#!/usr/bin/env python3
"""
Build clean Appendix 1 markdown with <mark> HTML highlighting.
V2: Position-based matching (start/end in plain text), boundary fixes.
"""
import re
import json
import os

BASE = '/home/z/my-project'
RAW_MD = os.path.join(BASE, 'upload', 'Appendix 1 - 20 pairs.md')
PAIRS_DIR = os.path.join(BASE, 'out', 'pairs')
OUT_DIR = os.path.join(BASE, 'out', 'appendix1')

CAT_COLORS = {
    'R': '#FFF3B0',   # yellow - Reference
    'S': '#C8E6C9',   # green  - Substitution
    'E': '#BBDEFB',   # blue   - Ellipsis
    'C': '#FFE0B2',   # orange - Conjunction
    'L': '#E1BEE7',   # purple - Lexical
}
CAT_EMOJI = {'R': '🟨', 'S': '🟩', 'E': '🟦', 'C': '🟧', 'L': '🟪'}
EMOJI_CLASS = '🟪🟨🟩🟦🟧'


def convert_to_mark(hl_text):
    """Convert emoji markup to <mark> HTML tags."""
    def repl(m):
        emoji = m.group(1)
        inner = m.group(2)
        for cat, e in CAT_EMOJI.items():
            if e == emoji:
                color = CAT_COLORS[cat]
                return f'<mark style="background-color:{color}">{inner}</mark>'
        return inner
    return re.sub(r'([' + EMOJI_CLASS + r'])⟦([^⟧]*)⟧', repl, hl_text)


def load_highlighted_body(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    idx = content.find('\n---\n')
    if idx != -1:
        return content[idx + 5:].lstrip('\n')
    return content.lstrip('\n')


def build_plain_and_map(hl_text):
    """
    Strip markup -> plain text + pos_map (plain_pos -> hl_pos).
    Ellipsis markers (inner == '∅') are skipped entirely.
    """
    plain_chars = []
    pos_map = []
    i = 0
    n = len(hl_text)
    while i < n:
        ch = hl_text[i]
        if ch in EMOJI_CLASS and i + 1 < n and hl_text[i+1] == '⟦':
            j = hl_text.find('⟧', i + 2)
            if j == -1:
                j = n
            inner = hl_text[i+2:j]
            if inner != '∅':
                for k, c in enumerate(inner):
                    plain_chars.append(c)
                    pos_map.append(i + 2 + k)
            i = j + 1
        else:
            plain_chars.append(ch)
            pos_map.append(i)
            i += 1
    pos_map.append(n)
    return ''.join(plain_chars), pos_map


def build_norm_index(text):
    """
    Collapse whitespace -> norm_text + norm_to_orig mapping.
    norm_to_orig[i] = orig position of norm char i; extra sentinel at end.
    Also normalizes curly quotes to straight (1:1 replacement, positions preserved).
    """
    # 1:1 character replacements (positions preserved)
    text = text.replace('\u201c', '"').replace('\u201d', '"')
    text = text.replace('\u2018', "'").replace('\u2019', "'")

    norm_chars = []
    norm_to_orig = []
    i = 0
    n = len(text)
    while i < n:
        if text[i].isspace():
            j = i
            while j < n and text[j].isspace():
                j += 1
            norm_chars.append(' ')
            norm_to_orig.append(i)
            i = j
        else:
            norm_chars.append(text[i])
            norm_to_orig.append(i)
            i += 1
    norm_to_orig.append(n)
    return ''.join(norm_chars), norm_to_orig


def normalize_for_match(text):
    """Normalize text for comparison. Strips markdown links first."""
    # Strip markdown links: [text](url) -> text
    text = re.sub(r'\[([^\]]*)\]\(([^)]*)\)', r'\1', text)
    # Strip orphan link remnants: ](url)
    text = re.sub(r'\]\([^)]*\)', '', text)
    # Remove markdown escapes
    text = text.replace('\\[', '[').replace('\\]', ']').replace('\\|', '|')
    # Remove bold/italic markers
    text = re.sub(r'\*\*([^*]*)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]*)\*', r'\1', text)
    # Normalize quotes
    text = text.replace('\u201c', '"').replace('\u201d', '"')
    text = text.replace('\u2018', "'").replace('\u2019', "'")
    # Collapse whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


class HighlightExtractor:
    """Manages position mapping and extraction for one highlighted file."""

    def __init__(self, hl_path):
        self.hl_body = load_highlighted_body(hl_path)
        self.plain, self.pos_map = build_plain_and_map(self.hl_body)
        self.norm_text, self.norm_to_orig = build_norm_index(self.plain)
        self.search_pos = 0  # in norm_text
        self.covered_end = 0  # track what's been covered

    def is_duplicate(self, raw_text):
        """Check if raw_text content was already covered by a previous match."""
        q = normalize_for_match(raw_text)
        if not q or len(q) < 20:
            return False
        # Check if query appears entirely before current search_pos
        # (i.e., in already-covered territory)
        check_limit = min(self.search_pos, len(self.norm_text))
        if check_limit <= 0:
            return False
        # Search in the covered region [0, search_pos)
        prefix = q[:min(60, len(q))]
        if len(prefix) < 15:
            return False
        idx = self.norm_text.find(prefix, 0, check_limit)
        if idx == -1:
            return False
        # Verify with suffix if possible
        if len(q) > 80:
            suffix = q[-40:]
            sidx = self.norm_text.find(suffix, idx, min(idx + len(q) + 200, check_limit))
            if sidx == -1:
                return False
        return True

    def find_range(self, raw_text):
        """
        Find raw_text in norm_text starting from self.search_pos.
        Returns (norm_start, norm_end) or None.
        Updates self.search_pos on success.
        Handles: heading+content merged, markdown links, minor text differences.
        """
        q = normalize_for_match(raw_text)
        if not q or len(q) < 10:
            return None

        # Strategy 1: full match
        idx = self.norm_text.find(q, self.search_pos)
        if idx != -1:
            self.search_pos = idx + len(q)
            return idx, idx + len(q)

        # Strategy 2: heading+content - try suffixes at sentence boundaries
        # Split by '. ' or '.**' or '?' to find where content starts
        for start_off in self._heading_offsets(q):
            sub = q[start_off:]
            if len(sub) < 30:
                continue
            idx = self.norm_text.find(sub[:80], self.search_pos)
            if idx != -1:
                # Verify: check suffix too
                suffix = sub[-40:]
                if len(suffix) > 15:
                    end_idx = self.norm_text.find(suffix, idx)
                    if end_idx != -1:
                        end = end_idx + len(suffix)
                        self.search_pos = end
                        return idx, end
                end = idx + len(sub)
                if end <= len(self.norm_text):
                    self.search_pos = end
                    return idx, end

        # Strategy 3: prefix match with suffix verification
        prefix = q[:60]
        if len(prefix) > 25:
            idx = self.norm_text.find(prefix, self.search_pos)
            if idx != -1:
                suffix = q[-40:]
                if len(suffix) > 15:
                    end_idx = self.norm_text.find(suffix, idx)
                    if end_idx != -1:
                        end = end_idx + len(suffix)
                        self.search_pos = end
                        return idx, end
                end = idx + len(q)
                self.search_pos = end
                return idx, end

        # Strategy 4: shorter prefix
        prefix = q[:35]
        if len(prefix) > 15:
            idx = self.norm_text.find(prefix, self.search_pos)
            if idx != -1:
                end = idx + len(q)
                if end <= len(self.norm_text):
                    self.search_pos = end
                    return idx, end

        # Strategy 5: word-by-word heading skip (skip up to 8 words from start)
        words = q.split(' ')
        for skip in range(2, min(12, len(words))):
            sub = ' '.join(words[skip:])
            if len(sub) < 40:
                break
            idx = self.norm_text.find(sub[:60], self.search_pos)
            if idx != -1:
                suffix = sub[-30:]
                end_idx = self.norm_text.find(suffix, idx) if len(suffix) > 12 else -1
                if end_idx != -1:
                    end = end_idx + len(suffix)
                else:
                    end = idx + len(sub)
                if end <= len(self.norm_text):
                    self.search_pos = max(end, idx + 30)
                    return idx, end

        # Strategy 6: search for END of query to advance position (for cascading fix)
        # If we can find the LAST sentence of the query, use that
        if len(q) > 100:
            last_sentence = q[-80:]
            idx = self.norm_text.find(last_sentence, self.search_pos)
            if idx != -1:
                end = idx + len(last_sentence)
                self.search_pos = end
                return idx, end

        return None

    def _heading_offsets(self, q):
        """Generate candidate offsets where heading ends and content begins."""
        offsets = []
        # After bold close: **Heading** Content
        for m in re.finditer(r'\*\*([^*]+)\*\*\s', q[:200]):
            offsets.append(m.end())
        # After ? or : followed by space (in first 150 chars - typical heading)
        for m in re.finditer(r'[?:.]\s', q[:150]):
            if m.start() > 10:
                offsets.append(m.end())
        # After first sentence
        m = re.search(r'\.\s', q[:150])
        if m and m.start() > 15:
            offsets.append(m.end())
        return sorted(set(o for o in offsets if 0 < o < len(q)))

    def extract(self, norm_start, norm_end):
        """Extract highlighted text for norm range [norm_start, norm_end)."""
        if norm_start >= len(self.norm_to_orig):
            return None
        plain_start = self.norm_to_orig[norm_start]
        if norm_end < len(self.norm_to_orig):
            plain_end = self.norm_to_orig[norm_end]
        else:
            plain_end = self.norm_to_orig[-1]

        # Word-boundary fix: if plain_start is mid-word, back up to word start
        while plain_start > 0 and plain_start < len(self.plain) and \
              self.plain[plain_start].isalnum() and self.plain[plain_start - 1].isalnum():
            plain_start -= 1

        # Word-boundary fix: if plain_end is mid-word, advance to word end
        while plain_end < len(self.plain) - 1 and \
              plain_end > 0 and self.plain[plain_end].isalnum() and self.plain[plain_end - 1].isalnum():
            plain_end += 1

        if plain_start >= len(self.pos_map) - 1:
            return None

        hl_start = self.pos_map[plain_start]
        hl_end = self.pos_map[plain_end] if plain_end < len(self.pos_map) - 1 else len(self.hl_body)

        # Boundary fix: back up hl_start to include markup opening if inside markup
        while hl_start > 0:
            prev = self.hl_body[hl_start - 1]
            if prev == '⟦':
                hl_start -= 2  # include ⟦ and emoji
                # Continue backing up over emoji
                continue
            elif prev in EMOJI_CLASS:
                hl_start -= 1
                # Check if char before emoji is ⟧ (end of previous markup) - stop
                if hl_start > 0 and self.hl_body[hl_start - 1] == '⟧':
                    hl_start += 1  # undo, we were at markup start already
                    break
                continue
            else:
                break

        # Boundary fix: extend hl_end to close any unclosed markup
        seg = self.hl_body[hl_start:hl_end]
        open_count = seg.count('⟦')
        close_count = seg.count('⟧')
        if open_count > close_count:
            # Extend to find closing ⟧
            j = self.hl_body.find('⟧', hl_end)
            if j != -1:
                hl_end = j + 1

        result = self.hl_body[hl_start:hl_end].strip()
        if not result:
            return None

        # Clean up any orphan ⟧ at start (shouldn't happen after fix, but just in case)
        while result.startswith('⟧'):
            result = result[1:]
        # Clean orphan emoji at end
        while result and result[-1] in EMOJI_CLASS:
            result = result[:-1]
        # If result has orphan ⟦ at end (unclosed), remove it
        if result.endswith('⟦'):
            result = result[:-1]
        if result.endswith('⟦'.replace('⟦', '')):
            pass

        # Final cleanup: check for balanced markup
        # Remove any stray ⟧ or ⟦ that are unbalanced
        result = self._clean_orphan_markers(result)

        return result if result else None

    def _clean_orphan_markers(self, text):
        """Remove orphan ⟧ markers (closing without opening)."""
        result = []
        depth = 0
        for ch in text:
            if ch == '⟦':
                depth += 1
                result.append(ch)
            elif ch == '⟧':
                if depth > 0:
                    depth -= 1
                    result.append(ch)
                # else: orphan, skip
            else:
                result.append(ch)
        # Remove unclosed ⟦ and preceding emoji
        result_str = ''.join(result)
        while result_str.endswith('⟦'):
            result_str = result_str[:-1]
            if result_str and result_str[-1] in EMOJI_CLASS:
                result_str = result_str[:-1]
        return result_str


# ============================================================
# Raw file parsing
# ============================================================

PAIR_BOUNDARIES = [
    ('P01', 1, 48), ('P02', 49, 97), ('P03', 98, 149), ('P04', 150, 198),
    ('P05', 199, 269), ('P06', 270, 305), ('P07', 306, 345), ('P08', 346, 381),
    ('P09', 382, 427), ('P10', 428, 474), ('P11', 475, 524), ('P12', 525, 533),
    ('P13', 534, 551), ('P14', 552, 567), ('P15', 568, 595), ('P16', 596, 615),
    ('P17', 616, 641), ('P18', 642, 660), ('P19', 661, 681), ('P20', 682, 719),
]

URL_LINES = {
    'P01': (3, 3), 'P02': (50, 50), 'P03': (98, 99), 'P04': (150, 152),
    'P05': (199, 201), 'P06': (270, 271), 'P07': (306, 307), 'P08': (346, 347),
    'P09': (382, 383), 'P10': (428, 429), 'P11': (475, 477), 'P12': (525, 527),
    'P13': (534, 535), 'P14': (552, 553), 'P15': (568, 569), 'P16': (596, 598),
    'P17': (616, 617), 'P18': (642, 643), 'P19': (661, 662), 'P20': (None, None),
}


def extract_url_from_line(line):
    m = re.search(r'\]\((https?://[^)]+)\)', line)
    if m:
        return m.group(1)
    m = re.search(r'(https?://\S+)', line)
    if m:
        return m.group(1).rstrip('\\').rstrip('.').rstrip(')')
    return None


def extract_urls_pair_from_line(line):
    """
    Extract (en_url, vi_url) from a line.
    If line is a table row with 2 cells, extract URL from each cell.
    Otherwise, extract URLs in order of appearance (EN first, VI second).
    """
    # Try table row parsing first
    cells = None
    s = line.strip()
    if s.startswith('|') and s.endswith('|') and s.count('|') >= 2:
        inner = s[1:s.rfind('|')]
        # Split by unescaped |
        parts = []
        current = ''
        i = 0
        while i < len(inner):
            if inner[i] == '\\' and i + 1 < len(inner) and inner[i+1] == '|':
                current += '|'
                i += 2
            elif inner[i] == '|':
                parts.append(current.strip())
                current = ''
                i += 1
            else:
                current += inner[i]
                i += 1
        parts.append(current.strip())
        if len(parts) >= 2:
            cells = parts[:2]

    if cells:
        en_url = None
        vi_url = None
        for cell in cells:
            m = re.search(r'\]\((https?://[^)]+)\)', cell)
            if not m:
                m = re.search(r'(https?://\S+)', cell)
                if m:
                    url = m.group(1).rstrip('\\').rstrip('.').rstrip(')')
                else:
                    continue
            else:
                url = m.group(1)
            if is_vi_url(url):
                vi_url = vi_url or url
            else:
                en_url = en_url or url
        return en_url, vi_url

    # Not a table row: extract URLs in order
    urls = re.findall(r'\]\((https?://[^)]+)\)', line) or re.findall(r'(https?://\S+)', line)
    urls = [u.rstrip('\\').rstrip('.').rstrip(')') for u in urls]
    en_url = None
    vi_url = None
    for url in urls:
        if is_vi_url(url):
            vi_url = vi_url or url
        else:
            en_url = en_url or url
    return en_url, vi_url


def is_vi_url(url):
    """Check if URL is a Vietnamese-language article."""
    return ('voatiengviet' in url or '/language/vietnamese/' in url or
            '/vi/article/' in url or 'tieng-viet' in url or 'vietnamese' in url)


def parse_table_cells(line):
    """Parse a markdown table row into cells, handling escaped pipes."""
    s = line.strip()
    if not (s.startswith('|') and s.endswith('|')):
        return None
    inner = s[1:-1]
    cells = []
    current = ''
    i = 0
    while i < len(inner):
        if inner[i] == '\\' and i + 1 < len(inner) and inner[i+1] == '|':
            current += '|'
            i += 2
        elif inner[i] == '|':
            cells.append(current.strip())
            current = ''
            i += 1
        else:
            current += inner[i]
            i += 1
    cells.append(current.strip())
    return cells if len(cells) >= 2 else None


HEADER_PATTERNS = {
    'tiếng anh', 'en', 'eng', 'english', 'anh', 'tieng anh',
}
HEADER_PATTERNS_VI = {
    'tiếng việt', 'vi', 'vie', 'vietnamese', 'việt', 'tieng viet',
}


def parse_raw_file():
    with open(RAW_MD, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    pairs = {}
    for pair_id, start, end in PAIR_BOUNDARIES:
        section = lines[start-1:end]

        en_url, vi_url = None, None
        url_lines = URL_LINES.get(pair_id, (None, None))
        # If both URLs are on the same line, extract as pair
        if url_lines[0] and url_lines[0] == url_lines[1]:
            en_url, vi_url = extract_urls_pair_from_line(lines[url_lines[0]-1])
        else:
            if url_lines[0]:
                # EN line: extract pair (in case both on same line)
                e, v = extract_urls_pair_from_line(lines[url_lines[0]-1])
                en_url = en_url or e
                vi_url = vi_url or v
            if url_lines[1]:
                e, v = extract_urls_pair_from_line(lines[url_lines[1]-1])
                en_url = en_url or e
                vi_url = vi_url or v

        rows = []
        for line in section:
            s = line.strip()
            if not s.startswith('|'):
                continue
            if ':---' in s:
                continue
            cells = parse_table_cells(s)
            if not cells or len(cells) != 2:
                continue
            en, vi = cells
            # Skip header rows
            en_l = normalize_for_match(en).lower()
            vi_l = normalize_for_match(vi).lower()
            if en_l in HEADER_PATTERNS and vi_l in HEADER_PATTERNS_VI:
                continue
            # Skip URL-only rows
            if en.startswith('https://') or vi.startswith('https://'):
                continue
            # Skip title rows
            if en.startswith('[**') and '**]' in en:
                continue
            if en == 'none' and vi == 'none':
                continue
            rows.append((en, vi))

        pairs[pair_id] = {'en_url': en_url, 'vi_url': vi_url, 'rows': rows}
    return pairs


# ============================================================
# Main build
# ============================================================

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print("Parsing raw markdown...")
    raw_pairs = parse_raw_file()

    print("Processing highlights...")
    all_output = []
    stats = {}
    issues = []

    # Document header
    all_output.append('# Appendix 1 — 20 cặp bài báo EN–VI (có đánh dấu ngữ nghĩa)')
    all_output.append('')
    all_output.append('**Chú giải màu (Legend):**')
    all_output.append('')
    all_output.append('| Màu | Ký hiệu | Danh mục (Halliday & Hasan 1976 / Trần Ngọc Thêm 2006) |')
    all_output.append('| :--- | :--- | :--- |')
    all_output.append('| <mark style="background-color:#FFF3B0">&nbsp;</mark> | R | Reference — tham chiếu (đại từ, chỉ từ) |')
    all_output.append('| <mark style="background-color:#C8E6C9">&nbsp;</mark> | S | Substitution — thay thế |')
    all_output.append('| <mark style="background-color:#BBDEFB">&nbsp;</mark> | E | Ellipsis — lược bỏ (∅ = vị trí trống) |')
    all_output.append('| <mark style="background-color:#FFE0B2">&nbsp;</mark> | C | Conjunction — liên kết |')
    all_output.append('| <mark style="background-color:#E1BEE7">&nbsp;</mark> | L | Lexical cohesion — liên kết từ vựng |')
    all_output.append('')

    for pair_num in range(1, 21):
        pair_id = f'P{pair_num:02d}'
        raw = raw_pairs[pair_id]

        with open(os.path.join(PAIRS_DIR, pair_id, 'meta.json'), 'r', encoding='utf-8') as f:
            meta = json.load(f)

        # Filter out title-duplicate rows
        title_en_norm = normalize_for_match(meta.get('title_en', ''))
        title_vi_norm = normalize_for_match(meta.get('title_vi', ''))
        filtered_rows = []
        for en_raw, vi_raw in raw['rows']:
            en_n = normalize_for_match(en_raw) if en_raw != 'none' else ''
            vi_n = normalize_for_match(vi_raw) if vi_raw != 'none' else ''
            en_is_title = bool(title_en_norm) and len(en_n) > 10 and \
                (en_n == title_en_norm or title_en_norm.startswith(en_n) or en_n.startswith(title_en_norm))
            vi_is_title = bool(title_vi_norm) and len(vi_n) > 10 and \
                (vi_n == title_vi_norm or title_vi_norm.startswith(vi_n) or vi_n.startswith(title_vi_norm))
            if en_is_title and vi_is_title:
                continue
            if (en_is_title and vi_raw == 'none') or (vi_is_title and en_raw == 'none'):
                continue
            filtered_rows.append((en_raw, vi_raw))

        # Create extractors
        st_ext = HighlightExtractor(os.path.join(PAIRS_DIR, pair_id, 'ST_highlighted.md'))
        tt_ext = HighlightExtractor(os.path.join(PAIRS_DIR, pair_id, 'TT_highlighted.md'))

        # Process rows
        processed = []
        en_match_count = 0
        vi_match_count = 0
        en_dup_count = 0
        vi_dup_count = 0
        for en_raw, vi_raw in filtered_rows:
            en_hl = None
            vi_hl = None
            skip_row = True

            if en_raw != 'none':
                if st_ext.is_duplicate(en_raw):
                    en_dup_count += 1
                    en_hl = '__DUPLICATE__'
                else:
                    rng = st_ext.find_range(en_raw)
                    if rng:
                        en_hl = st_ext.extract(rng[0], rng[1])
                        if en_hl:
                            en_match_count += 1
            if vi_raw != 'none':
                if tt_ext.is_duplicate(vi_raw):
                    vi_dup_count += 1
                    vi_hl = '__DUPLICATE__'
                else:
                    rng = tt_ext.find_range(vi_raw)
                    if rng:
                        vi_hl = tt_ext.extract(rng[0], rng[1])
                        if vi_hl:
                            vi_match_count += 1

            # Skip row if BOTH sides are duplicates
            if en_hl == '__DUPLICATE__' and vi_hl == '__DUPLICATE__':
                continue
            # Skip if one side is duplicate and other is 'none'
            if (en_hl == '__DUPLICATE__' and vi_raw == 'none') or \
               (vi_hl == '__DUPLICATE__' and en_raw == 'none'):
                continue

            processed.append((en_raw, vi_raw, en_hl, vi_hl))

        total_en = sum(1 for e, v, _, _ in processed if e != 'none')
        total_vi = sum(1 for e, v, _, _ in processed if v != 'none')
        stats[pair_id] = {
            'rows': len(processed),
            'en_total': total_en, 'en_matched': en_match_count,
            'vi_total': total_vi, 'vi_matched': vi_match_count,
            'en_dups': en_dup_count, 'vi_dups': vi_dup_count,
        }

        if en_match_count < total_en * 0.8 or vi_match_count < total_vi * 0.8:
            issues.append(f"{pair_id}: EN {en_match_count}/{total_en}, VI {vi_match_count}/{total_vi}")

        print(f"  {pair_id}: EN {en_match_count}/{total_en}, VI {vi_match_count}/{total_vi}")

        # Generate markdown
        all_output.append(f'## Pair {pair_num:02d}')
        all_output.append('')

        en_url = raw['en_url'] or ''
        vi_url = raw['vi_url'] or ''
        en_header = f'[EN]({en_url})' if en_url else 'EN'
        vi_header = f'[VI]({vi_url})' if vi_url else 'VI'

        all_output.append(f'| {en_header} | {vi_header} |')
        all_output.append('| :--- | :--- |')

        title_en = meta.get('title_en', '')
        title_vi = meta.get('title_vi', '')
        if title_en or title_vi:
            te = title_en.replace('|', '\\|')
            tv = title_vi.replace('|', '\\|')
            all_output.append(f'| **{te}** | **{tv}** |')

        for en_raw, vi_raw, en_hl, vi_hl in processed:
            # Use highlighted if available; duplicates become empty (content shown elsewhere)
            if en_hl == '__DUPLICATE__':
                en_cell = ''
            else:
                en_cell = en_hl if en_hl else (en_raw if en_raw != 'none' else '')
            if vi_hl == '__DUPLICATE__':
                vi_cell = ''
            else:
                vi_cell = vi_hl if vi_hl else (vi_raw if vi_raw != 'none' else '')

            # Convert emoji markup to <mark>
            en_cell = convert_to_mark(en_cell)
            vi_cell = convert_to_mark(vi_cell)

            # Clean for table cell
            def clean_cell(c):
                c = c.replace('\n', ' ')
                c = re.sub(r'  +', ' ', c)
                # Escape pipes (but not inside <mark> tags - there are no pipes in tags)
                c = c.replace('|', '\\|')
                return c.strip()

            en_cell = clean_cell(en_cell)
            vi_cell = clean_cell(vi_cell)

            if en_cell or vi_cell:
                all_output.append(f'| {en_cell} | {vi_cell} |')

        all_output.append('')

    # Write
    output_path = os.path.join(OUT_DIR, 'Appendix1_marked.md')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(all_output))

    print(f"\nOutput: {output_path} ({len(all_output)} lines)")

    if issues:
        print("\nPairs with low match rates:")
        for iss in issues:
            print(f"  {iss}")

    with open(os.path.join(OUT_DIR, 'match_stats.json'), 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
