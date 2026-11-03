#!/usr/bin/env python3
"""
Appendix 1 builder — V3 (multi-colour <span> highlighting).

Inputs
  upload/Appendix 1 - 20 pairs.md          reference layout (2-col EN|VI rows)
  out/pairs/PXX/ST_highlighted.md          emoji+⟦⟧ marked ST (from render.py)
  out/pairs/PXX/TT_highlighted.md          emoji+⟦⟧ marked TT
  out/pairs/PXX/{ST,TT}_{seg,ties}.json    sentence segments + tie tables (tooltips)

Outputs (out/appendix1/)
  Appendix1.md              markdown, 5-colour <span style> highlights, 2-col tables
  Appendix1.html            standalone HTML, 2-col tables, colours + tie tooltips
  appendix1_segments.json   intermediate representation (consumed by export_docx.py)
  match_stats.json          row matching + marker coverage statistics

Position model: markers parsed from the emoji markup live in *plain* coordinates
(plain text == ST.txt/TT.txt flow, since markers are pure insertions), which are
identical to the flow coordinates used by render.py — so a marker's start
position maps 1:1 onto its tie's computed (fa) position for tooltips.
"""
import re
import json
import os
import html as H
import difflib

import os as _os
BASE = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
RAW_MD = os.path.join(BASE, 'upload', 'Appendix 1 - 20 pairs.md')
PAIRS_DIR = os.path.join(BASE, 'out', 'pairs')
OUT_DIR = os.path.join(BASE, 'out', 'appendix1')

CATS = {
    'R': {'bg': '#FFF3B0', 'fg': '#664D03', 'emoji': '🟨', 'en': 'Reference',
          'vi': 'tham chiếu (đại từ, chỉ từ)'},
    'S': {'bg': '#C8E6C9', 'fg': '#14532D', 'emoji': '🟩', 'en': 'Substitution',
          'vi': 'thay thế'},
    'E': {'bg': '#BBDEFB', 'fg': '#1E3A8A', 'emoji': '🟦', 'en': 'Ellipsis',
          'vi': 'lược bỏ (∅ = vị trí trống)'},
    'C': {'bg': '#FFE0B2', 'fg': '#7C2D12', 'emoji': '🟧', 'en': 'Conjunction',
          'vi': 'liên kết'},
    'L': {'bg': '#E1BEE7', 'fg': '#581C87', 'emoji': '🟪', 'en': 'Lexical cohesion',
          'vi': 'liên kết từ vựng'},
}
CAT_EMOJI = {c['emoji']: k for k, c in CATS.items()}
EMOJI_CLASS = ''.join(CAT_EMOJI)

REF_NAMES = {'A': 'anaphoric', 'C': 'cataphoric', 'E': 'exophoric'}

# H&H (1976) category <-> Trần Ngọc Thêm (2006) device correspondence
FRAMEWORK_MAP = [
    ('R', 'reference (personal, demonstrative, comparative, quantified)',
     'phép thế đại từ (đại từ / chỉ từ) — cùng nhóm với S'),
    ('S', 'substitution (nominal, verbal, clausal)',
     'phép thế đại từ (phần thế danh từ / động từ / mệnh đề)'),
    ('E', 'ellipsis', 'phép tỉnh lược'),
    ('C', 'conjunction (adversative, additive, temporal, causal)',
     'phép nối'),
    ('L', 'lexical cohesion (repetition, synonymy, antonymy, collocation)',
     'phép lặp, phép đối, phép thế đồng nghĩa, phép liên tưởng'),
]

DOC_TITLE = 'Appendix 1 — 20 cặp bài báo EN–VI (có đánh dấu ngữ nghĩa)'
INTRO = ('Bản tiếng Anh (EN) đánh dấu theo Halliday & Hasan (1976); bản tiếng Việt (VI) '
         'đánh dấu theo Trần Ngọc Thêm (2006, dẫn theo Nguyễn Thanh Tùng 2020), quy về '
         'cùng thang 5 màu. Bản này đánh dấu các tie liên-câu (R/C/L) và '
         'BỔ SUNG THỦ CÔNG các vị trí phép thế (S) / phép tỉnh lược (E) đã được '
         'phân tích trong download/BDNC/semantic_analysis — gồm cả [LC] liên câu '
         'và [TC] trong câu; level được ghi trong tooltip/comment từng khối.')
MD_NOTE = ('> **Lưu ý hiển thị:** GitHub lọc bỏ thuộc tính `style` inline nên trên GitHub '
           'các đoạn đánh dấu trong file `.md` có thể không hiện màu. Bản màu đầy đủ: xem '
           'file **`.html`** (rê chuột để xem chi tiết liên kết) hoặc **`.docx`** đính kèm. '
           'Ký hiệu ∅ (nền xanh) = vị trí trống của phép lược bỏ (E). '
           'S/E được bổ sung thủ công từ 20 bản phân tích ngữ nghĩa: [LC] = liên câu, '
           '[TC] = trong câu (xem tooltip/comment).')


# ============================================================
# Marked-text scanning (emoji + ⟦⟧  ->  plain text + markers)
# ============================================================

def load_highlighted_body(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    idx = content.find('\n---\n')
    if idx != -1:
        return content[idx + 5:].lstrip('\n')
    return content.lstrip('\n')


def scan_marked(hl_text):
    """Scan emoji+⟦⟧ markup -> (plain_text, markers in plain coordinates).

    Text markers: {'fa', 'fb', 'cat', 'point': False}
    Ellipsis points: {'fa' == 'fb', 'cat': 'E', 'point': True}
    """
    plain = []
    markers = []
    i, n = 0, len(hl_text)
    while i < n:
        ch = hl_text[i]
        if ch in EMOJI_CLASS and i + 1 < n and hl_text[i + 1] == '⟦':
            j = hl_text.find('⟧', i + 2)
            if j == -1:
                j = n
            inner = hl_text[i + 2:j]
            cat = CAT_EMOJI[ch]
            if inner == '∅':
                markers.append({'fa': len(plain), 'fb': len(plain),
                                'cat': cat, 'point': True})
            else:
                fa = len(plain)
                plain.extend(inner)
                markers.append({'fa': fa, 'fb': len(plain),
                                'cat': cat, 'point': False})
            i = j + 1
        else:
            plain.append(ch)
            i += 1
    return ''.join(plain), markers


# ============================================================
# Tie positions (flow coordinates) for tooltips
# ============================================================

def load_ties_with_positions(pair_id, pref):
    """Replicates render.py's position computation.

    Returns (text_ties_by_fa, point_ties_by_pos, n_ties).
    """
    d = os.path.join(PAIRS_DIR, pair_id)
    seg = json.load(open(f'{d}/{pref}_seg.json'))
    ties = json.load(open(f'{d}/{pref}_ties.json'))['ties']
    sents = {s['id']: s for s in seg['sentences']}
    text_map, point_map = {}, {}
    for t in ties:
        s = sents.get(t['sent'])
        if s is None:
            continue
        if t['text'] is None:
            pos, found, p = -1, 0, -1
            while True:
                p = s['text'].find(t['gap_after'], p + 1)
                if p < 0:
                    break
                found += 1
                if found == t['occ']:
                    pos = p + len(t['gap_after'])
                    break
            if pos >= 0:
                point_map.setdefault(s['fa'] + pos, t)
        else:
            p, found, a = -1, 0, -1
            while True:
                p = s['text'].find(t['text'], p + 1)
                if p < 0:
                    break
                found += 1
                if found == t['occ']:
                    a = p
                    break
            if a >= 0:
                text_map.setdefault(s['fa'] + a, t)
    return text_map, point_map, len(ties)


def tie_tip(t):
    if t is None:
        return None
    c = CATS[t['cat']]
    dirbit = ''
    if t['cat'] == 'R':
        r = t.get('ref')
        if r in REF_NAMES:
            dirbit = f" | dir: {REF_NAMES[r]} ({r})"
    if t.get('text') is None:
        tip = (f"{c['en']} ({t['cat']}/{t.get('sub', '')}) | gap after: "
               f"{t.get('gap_after', '')} | recovered: {t.get('recovered', '')} | "
               f"ante: {t.get('ante', '')}")
    else:
        tip = (f"{c['en']} ({t['cat']}/{t.get('sub', '')}){dirbit} | ante: "
               f"{t.get('ante', '')} | conf={t.get('conf', '')}")
        if t.get('alt'):
            tip += f" | alt: {t['alt']}"
    tip += f" | level: {t.get('level','LC')}"
    if t.get('note'):
        tip += f" | note: {t['note']}"
    return tip


# ============================================================
# Normalisation / matching (unchanged from V2)
# ============================================================

def build_norm_index(text):
    """Collapse whitespace -> norm_text + norm_to_orig mapping."""
    text = text.replace('\u201c', '"').replace('\u201d', '"')
    text = text.replace('\u2018', "'").replace('\u2019', "'")
    norm_chars, norm_to_orig = [], []
    i, n = 0, len(text)
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
    text = re.sub(r'\[([^\]]*)\]\(([^)]*)\)', r'\1', text)
    text = re.sub(r'\]\([^)]*\)', '', text)
    text = text.replace('\\[', '[').replace('\\]', ']').replace('\\|', '|')
    text = re.sub(r'\*\*([^*]*)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]*)\*', r'\1', text)
    text = text.replace('\u201c', '"').replace('\u201d', '"')
    text = text.replace('\u2018', "'").replace('\u2019', "'")
    text = re.sub(r'\s+', ' ', text).strip()
    return text


class HighlightExtractor:
    """Row matching + segment extraction for one highlighted file."""

    def __init__(self, hl_path, pair_id, pref):
        self.hl_body = load_highlighted_body(hl_path)
        self.plain, self.markers = scan_marked(self.hl_body)
        self.norm_text, self.norm_to_orig = build_norm_index(self.plain)
        self.search_pos = 0
        self.text_ties, self.point_ties, self.n_ties = \
            load_ties_with_positions(pair_id, pref)
        self.consumed = set()
        self.rendered = 0
        self.rendered_by_cat = {}
        self.straddles = 0
        self.orphan_markers = 0
        self.deferred = 0

    # ---------- duplicate / range finding (V2 logic) ----------

    def is_duplicate(self, raw_text):
        q = normalize_for_match(raw_text)
        if not q or len(q) < 20:
            return False
        check_limit = min(self.search_pos, len(self.norm_text))
        if check_limit <= 0:
            return False
        prefix = q[:min(60, len(q))]
        if len(prefix) < 15:
            return False
        idx = self.norm_text.find(prefix, 0, check_limit)
        if idx == -1:
            return False
        if len(q) > 80:
            suffix = q[-40:]
            sidx = self.norm_text.find(suffix, idx, min(idx + len(q) + 200, check_limit))
            if sidx == -1:
                return False
        return True

    # ---------- range finding (V3: validated candidates + fuzzy) ----------

    def find_range(self, raw_text):
        """Find the norm-text range covering a raw reference cell.

        Returns (norm_start, norm_end, q_offset, raw_prefix) or None.
        PURE: does not mutate self.search_pos (side_ir commits it).

        q_offset  – char offset in the normalized query where the match starts
                    (>0 when a leading part of the cell – typically a subhead
                    merged into the cell – is absent from the plain text)
        raw_prefix– the skipped query head, rendered as plain text so the
                    reference layout is preserved
        """
        q = normalize_for_match(raw_text)
        if not q or len(q) < 10:
            return None
        sp = self.search_pos
        N = self.norm_text

        # 1) exact verbatim match
        idx = N.find(q, sp)
        if idx != -1:
            return idx, idx + len(q), 0, ''

        # 2) heading offsets (bold subhead from the raw cell + punctuation)
        for off in self._heading_offsets(raw_text, q):
            sub = q[off:]
            if len(sub) < 30:
                continue
            cand = self._match_sub(sub, sp, off)
            if cand:
                return cand

        # 3) skip leading words (merged heading+content cells; subheads were
        #    stripped from the plain text during extraction)
        words = q.split(' ')
        offs, acc = [], 0
        for w in words:
            offs.append(acc)
            acc += len(w) + 1
        for skip in range(2, min(17, len(words))):
            sub = ' '.join(words[skip:])
            if len(sub) < 40:
                break
            cand = self._match_sub(sub, sp, offs[skip])
            if cand:
                return cand

        # 4) whole-query prefixes (short anchor, end via suffix/alignment)
        for plen in (60, 35):
            prefix = q[:plen]
            if len(q) <= plen or len(prefix) <= 15:
                continue
            idx = N.find(prefix, sp)
            if idx != -1:
                cand = self._match_from(idx, q, 0)
                if cand:
                    return cand

        # 5) trailing sentence
        if len(q) > 100:
            tail = q[-80:]
            idx = N.find(tail, sp)
            if idx != -1:
                return idx, idx + len(tail), len(q) - len(tail), ''

        # 6) fuzzy word-walk (PDF lost characters in the plain text)
        cand = self._fuzzy_find(q, sp)
        if cand:
            return cand
        return None

    def _match_sub(self, sub, sp, off):
        """Anchor on the first ~80 chars of sub; end via suffix + alignment."""
        N = self.norm_text
        idx = N.find(sub[:80], sp)
        if idx == -1:
            return None
        end, confirmed = self._sub_end(idx, sub)
        end = self._align_validate(idx, end, sub, confirmed)
        if end is None:
            return None
        return idx, end, off, ''

    def _match_from(self, idx, q, off):
        portion = q[off:]
        end, confirmed = self._sub_end(idx, portion)
        end = self._align_validate(idx, end, portion, confirmed)
        if end is None:
            return None
        return idx, end, off, ''

    def _sub_end(self, idx, portion):
        N = self.norm_text
        suffix = portion[-40:]
        if len(suffix) > 15:
            eidx = N.find(suffix, idx)
            if eidx != -1 and eidx < idx + len(portion) + 200:
                return eidx + len(suffix), True
        return idx + len(portion), False

    def _align_validate(self, a, end, portion, end_confirmed):
        """Align `portion` against norm_text[a:...].

        Rejects gross mismatches (coverage < 0.55 — e.g. a prefix that landed
        on unrelated text), and trims ends that ran past the true content
        (blind idx+len(q) ends, or a suffix that matched far too late).
        """
        N = self.norm_text
        window_end = min(a + len(portion) + 250, len(N))
        window = N[a:window_end]
        sm = difflib.SequenceMatcher(None, window, portion, autojunk=False)
        blocks = sm.get_matching_blocks()
        cov = sum(b.size for b in blocks) / max(1, len(portion))
        if cov < 0.55:
            return None
        # a valid row match must contain one substantial verbatim stretch —
        # scattered short matches (shared function words) are a false hit
        largest = max((b.size for b in blocks), default=0)
        if largest < max(20, 0.35 * len(portion)):
            return None
        solid = [b for b in blocks if b.size >= 5]
        if solid:
            trim_end = min(a + max(b.a + b.size for b in solid), window_end)
            if trim_end + 30 <= end:
                end = trim_end          # end ran well past the aligned content
            elif not end_confirmed and a + 20 <= trim_end < end:
                end = trim_end          # blind end: snap to alignment end
        return min(end, window_end)

    def _fuzzy_find(self, q, sp):
        """Word-walk alignment for PDF character loss (plain text is missing
        characters that the reference cell still has). Anchors on the longest
        verbatim word run, then walks word by word allowing fuzzy words."""
        N = self.norm_text
        words = q.split(' ')
        n = len(words)
        if n < 8 or len(q) < 60:
            return None
        offs, acc = [], 0
        for w in words:
            offs.append(acc)
            acc += len(w) + 1
        max_skip = min(16, max(0, n - 6))
        for skip in range(0, max_skip + 1):
            rem = words[skip:]
            for k in range(min(len(rem), 14), 3, -1):
                anchor = ' '.join(rem[:k])
                idx = N.find(anchor, sp)
                if idx == -1:
                    continue
                p = idx + len(anchor)
                wi = skip + k
                matched = k
                miss = 0
                while wi < n:
                    m = re.match(r'\s*(\S+)', N[p:])
                    if not m:
                        break
                    pw = m.group(1)
                    if pw == words[wi] or self._word_close(pw, words[wi]):
                        p += len(m.group(0))
                        matched += 1
                        miss = 0
                        wi += 1
                    else:
                        miss += 1
                        if miss > 2:
                            break
                        p += len(m.group(0))
                if wi >= n - 1 and matched >= n * 0.8:
                    m = re.match(r'[.,;:!?"”\')]*', N[p:])
                    if m:
                        p += len(m.group(0))
                    return idx, min(p, len(N)), offs[skip], \
                        q[:offs[skip]].rstrip()
        return None

    @staticmethod
    def _word_close(pw, w):
        """Fuzzy word equality tolerating lost characters on one side."""
        if not pw or not w:
            return False
        lo, hi = (pw, w) if len(pw) <= len(w) else (w, pw)
        if len(lo) < 2 or len(lo) / len(hi) < 0.6:
            return False
        if difflib.SequenceMatcher(None, lo, hi).ratio() >= 0.8:
            return True
        if len(lo) >= 4:                      # subsequence = char loss
            it = iter(hi)
            return all(c in it for c in lo)
        return False

    def _heading_offsets(self, raw_text, q):
        offsets = []
        m = re.match(r'\s*\*\*([^*]+)\*\*\s', raw_text)
        if m:
            h = normalize_for_match(m.group(1))
            if h and len(h) < 120:
                offsets.append(len(h) + 1)
        for m in re.finditer(r'\*\*([^*]+)\*\*\s', q[:200]):
            offsets.append(m.end())
        for m in re.finditer(r'[?:.]\s', q[:150]):
            if m.start() > 10:
                offsets.append(m.end())
        m = re.search(r'\.\s', q[:150])
        if m and m.start() > 15:
            offsets.append(m.end())
        return sorted(set(o for o in offsets if 0 < o < len(q)))

    # ---------- gap repair & duplicate retry (V3) ----------

    def plain_of(self, norm_pos):
        return self.norm_to_orig[min(norm_pos, len(self.norm_to_orig) - 1)]

    def markers_in(self, norm_a, norm_b):
        """Unconsumed markers whose start lies in [norm_a, norm_b)."""
        pa, pb = self.plain_of(norm_a), self.plain_of(norm_b)
        return [(i, m) for i, m in enumerate(self.markers)
                if i not in self.consumed and pa <= m['fa'] < pb]

    def repair_gap(self, rng, raw_text):
        """A fallback match landed at `a` but left unconsumed markers in the
        gap [search_pos, a). If the gap fuzzily matches the skipped query
        prefix, extend the range start over the gap so the markers render.

        Returns (new_start, raw_prefix) or None.
        """
        a, b, off, q_raw_prefix = rng
        q = normalize_for_match(raw_text)
        sp = self.search_pos
        if off <= 0 or a <= sp or (a - sp) > 350:
            return None
        if not self.markers_in(sp, a):
            return None
        gap = self.norm_text[sp:a]
        q_prefix = q[:off]
        sm = difflib.SequenceMatcher(None, gap, q_prefix, autojunk=False)
        blocks = sm.get_matching_blocks()
        cov = sum(bl.size for bl in blocks) / max(1, len(gap))
        # the gap must connect seamlessly to the match start; the joining
        # block scales with the gap size (small gaps: small blocks)
        need = min(15, max(4, int(len(gap) * 0.5)))
        junction = any(bl.a + bl.size >= len(gap) - 2 and bl.size >= need
                       for bl in blocks)
        if not junction or cov < 0.6:
            return None
        raw_prefix = ''
        first = next((bl for bl in blocks if bl.size >= 4), None)
        if first is not None and first.a == 0 and first.b > 0:
            raw_prefix = q[:first.b]
        return sp, raw_prefix.rstrip()

    # ---------- segment extraction (V3) ----------

    def segments(self, norm_start, norm_end):
        """Build the segment list for a norm-text range [norm_start, norm_end)."""
        ps = self.norm_to_orig[norm_start]
        if norm_end < len(self.norm_to_orig):
            pe = self.norm_to_orig[norm_end]
        else:
            pe = self.norm_to_orig[-1]
        while ps > 0 and ps < len(self.plain) and \
                self.plain[ps].isalnum() and self.plain[ps - 1].isalnum():
            ps -= 1
        while pe < len(self.plain) - 1 and pe > 0 and \
                self.plain[pe].isalnum() and self.plain[pe - 1].isalnum():
            pe += 1

        ms = []
        for idx, m in enumerate(self.markers):
            if idx in self.consumed:
                continue
            if m['point']:
                if ps <= m['fa'] <= pe:
                    ms.append(m)
                    self.consumed.add(idx)
            else:
                if ps <= m['fa'] < pe:
                    inside = pe - m['fa']
                    total = m['fb'] - m['fa']
                    if m['fb'] <= pe or inside >= max(3, (total + 1) // 2):
                        ms.append(m)
                        self.consumed.add(idx)
                        if m['fb'] > pe:
                            # marker text runs past the range end: complete it
                            if m['fb'] <= pe + 60:
                                pe = m['fb']
                            else:
                                self.straddles += 1
                    else:
                        # barely inside (range end stuck into the next row's
                        # marker) — leave it for the row that owns it
                        self.deferred += 1
        ms.sort(key=lambda m: (m['fa'], m['fb']))

        segs, last = [], ps
        for m in ms:
            if m['fa'] > last:
                segs.append({'t': self.plain[last:m['fa']]})
            if m['point']:
                tie = self.point_ties.get(m['fa'])
                if tie is None:
                    self.orphan_markers += 1
                segs.append({'t': '∅', 'cat': m['cat'], 'point': True,
                             'tip': tie_tip(tie),
                             'id': tie['id'] if tie else None})
            else:
                tie = self.text_ties.get(m['fa'])
                if tie is None:
                    self.orphan_markers += 1
                text = self.plain[m['fa']:min(m['fb'], pe)]
                segs.append({'t': text, 'cat': m['cat'], 'point': False,
                             'tip': tie_tip(tie),
                             'ref': (tie.get('ref') if tie and tie['cat'] == 'R'
                                     else None),
                             'id': tie['id'] if tie else None})
            last = max(last, m['fb'])
            self.rendered += 1
            self.rendered_by_cat[m['cat']] = self.rendered_by_cat.get(m['cat'], 0) + 1
        if pe > last:
            segs.append({'t': self.plain[last:pe]})
        if segs:
            segs[0]['t'] = segs[0]['t'].lstrip()
            segs[-1]['t'] = segs[-1]['t'].rstrip()
            segs = [s for s in segs if s['t']]
        return segs


# ============================================================
# Raw reference-file parsing (unchanged from V2)
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

HEADER_PATTERNS = {
    'tiếng anh', 'en', 'eng', 'english', 'anh', 'tieng anh',
}
HEADER_PATTERNS_VI = {
    'tiếng việt', 'vi', 'vie', 'vietnamese', 'việt', 'tieng viet',
}


def extract_urls_pair_from_line(line):
    cells = None
    s = line.strip()
    if s.startswith('|') and s.endswith('|') and s.count('|') >= 2:
        inner = s[1:s.rfind('|')]
        parts, current, i = [], '', 0
        while i < len(inner):
            if inner[i] == '\\' and i + 1 < len(inner) and inner[i + 1] == '|':
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
        en_url, vi_url = None, None
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
    urls = re.findall(r'\]\((https?://[^)]+)\)', line) or \
        re.findall(r'(https?://\S+)', line)
    urls = [u.rstrip('\\').rstrip('.').rstrip(')') for u in urls]
    en_url, vi_url = None, None
    for url in urls:
        if is_vi_url(url):
            vi_url = vi_url or url
        else:
            en_url = en_url or url
    return en_url, vi_url


def is_vi_url(url):
    return ('voatiengviet' in url or '/language/vietnamese/' in url or
            '/vi/article/' in url or 'tieng-viet' in url or 'vietnamese' in url)


def parse_table_cells(line):
    s = line.strip()
    if not (s.startswith('|') and s.endswith('|')):
        return None
    inner = s[1:-1]
    cells, current, i = [], '', 0
    while i < len(inner):
        if inner[i] == '\\' and i + 1 < len(inner) and inner[i + 1] == '|':
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


def parse_raw_file():
    with open(RAW_MD, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    pairs = {}
    for pair_id, start, end in PAIR_BOUNDARIES:
        section = lines[start - 1:end]
        en_url, vi_url = None, None
        url_lines = URL_LINES.get(pair_id, (None, None))
        if url_lines[0] and url_lines[0] == url_lines[1]:
            en_url, vi_url = extract_urls_pair_from_line(lines[url_lines[0] - 1])
        else:
            if url_lines[0]:
                e, v = extract_urls_pair_from_line(lines[url_lines[0] - 1])
                en_url = en_url or e
                vi_url = vi_url or v
            if url_lines[1]:
                e, v = extract_urls_pair_from_line(lines[url_lines[1] - 1])
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
            en_l = normalize_for_match(en).lower()
            vi_l = normalize_for_match(vi).lower()
            if en_l in HEADER_PATTERNS and vi_l in HEADER_PATTERNS_VI:
                continue
            if en.startswith('https://') or vi.startswith('https://'):
                continue
            if en.startswith('[**') and '**]' in en:
                continue
            if en == 'none' and vi == 'none':
                continue
            rows.append((en, vi))
        pairs[pair_id] = {'en_url': en_url, 'vi_url': vi_url, 'rows': rows}
    return pairs


# ============================================================
# Renderers
# ============================================================

def span_open_md(cat):
    c = CATS[cat]
    return (f'<span style="background-color:{c["bg"]};color:{c["fg"]};'
            f'padding:1px 4px;border-radius:3px">')


def clean_cell(c):
    c = c.replace('\n', ' ')
    c = re.sub(r'  +', ' ', c)
    c = c.replace('|', '\\|')
    return c.strip()


def md_side(side):
    """Render one table cell (markdown) from a side IR."""
    if side['kind'] in ('none', 'dup'):
        return ''
    if side['kind'] == 'raw':
        return clean_cell(side['text'])
    parts = []
    for s in side['segs']:
        if s.get('cat'):
            sup = (f"<sup>{s['ref']}</sup>"
                   if s['cat'] == 'R' and s.get('ref') else '')
            parts.append(span_open_md(s['cat']) + s['t'] + sup + '</span>')
        else:
            parts.append(s['t'])
    return clean_cell(''.join(parts))


MD_INLINE_PAT = re.compile(r'(\[[^\]]+\]\([^)]+\))|(\*\*[^*]+\*\*)')


def md_inline_html(text):
    """Minimal markdown inline -> HTML for raw fallback cells."""
    out, i = [], 0
    for m in MD_INLINE_PAT.finditer(text):
        out.append(H.escape(text[i:m.start()]))
        tok = m.group(0)
        if tok.startswith('['):
            mm = re.match(r'\[([^\]]+)\]\(([^)]+)\)', tok)
            out.append(f'<a href="{H.escape(mm.group(2), quote=True)}">'
                       f'{H.escape(mm.group(1))}</a>')
        else:
            out.append('<b>' + H.escape(tok[2:-2]) + '</b>')
        i = m.end()
    out.append(H.escape(text[i:]))
    return ''.join(out).replace('\\|', '|').replace('\n', ' ')


def html_side(side):
    """Render one table cell (HTML) from a side IR."""
    if side['kind'] in ('none', 'dup'):
        return ''
    if side['kind'] == 'raw':
        return md_inline_html(side['text'])
    parts = []
    for s in side['segs']:
        if s.get('cat'):
            c = CATS[s['cat']]
            attrs = (f'class="tie" style="background-color:{c["bg"]};'
                     f'color:{c["fg"]}"')
            if s.get('tip'):
                attrs += f' title="{H.escape(s["tip"], quote=True)}"'
            sup = (f'<sup>{s["ref"]}</sup>'
                   if s['cat'] == 'R' and s.get('ref') else '')
            parts.append(f'<span {attrs}>{H.escape(s["t"])}{sup}</span>')
        else:
            parts.append(H.escape(s['t']))
    return ''.join(parts).replace('\n', ' ')


HTML_CSS = '''<!DOCTYPE html>
<html lang="vi">
<head><meta charset="utf-8">
<title>__TITLE__</title>
<style>
body { font-family: Georgia, 'Times New Roman', serif; max-width: 1150px;
       margin: 2em auto; padding: 0 1.5em; line-height: 1.75; color: #1b1b1b; }
h1 { font-size: 1.45em; }
h2 { font-size: 1.15em; border-bottom: 2px solid #444; padding-bottom: .25em;
     margin-top: 2.8em; }
p.note { color: #555; font-size: .93em; }
table { border-collapse: collapse; width: 100%; table-layout: fixed;
        margin: 1em 0 2.5em; }
th, td { border: 1px solid #c9c9c9; vertical-align: top; padding: 6px 10px;
         width: 50%; }
th { background: #efefef; text-align: center; font-family: Arial, sans-serif; }
tr.titles td { background: #fafafa; }
span.tie { padding: 0 3px; border-radius: 3px; cursor: help; }
span.tie sup { font-size: .75em; font-weight: bold; }
table.framework { font-size: .92em; }
table.framework th, table.framework td { width: auto; }
.legend { margin: 1.2em 0; }
.legend span.tie { margin-right: .6em; padding: 1px 6px; }
a { color: #0b57d0; }
</style></head>
<body>
<h1>__TITLE__</h1>
<p>__INTRO__ Rê chuột lên đoạn được đánh dấu để xem chi tiết (danh mục, tiền trạm, độ tin cậy).</p>
<p class="legend">__LEGEND__</p>
<p class="note">Ký hiệu ∅ với nền xanh = vị trí trống của phép lược bỏ (E).</p>
'''


def build_html_doc(pair_sections):
    legend = ' '.join(
        f'<span class="tie" style="background-color:{c["bg"]};color:{c["fg"]}">'
        f'{k} — {c["en"]} ({c["vi"]})</span>'
        for k, c in CATS.items())
    ref_note = ('<p class="note"><b>Hướng tham chiếu (R):</b> mỗi khối R kèm '
                'chữ mũ — <b>A</b> = anaphoric (hồi quy: tiền trạm nằm trước '
                'trong văn bản), <b>C</b> = cataphoric (tiến chỉ: tiền trạm nằm '
                'sau), <b>E</b> = exophoric (ngoại văn bản: tiền trạm trong bối '
                'cảnh phát ngôn — người viết / độc giả). Toàn ngữ liệu không có '
                'trường hợp C liên-câu. Chữ mũ E này khác ký hiệu danh mục '
                '<span class="tie" style="background-color:#BBDEFB;color:#1E3A8A">'
                'E</span> = lược bỏ.</p>')
    fw_rows = '\n'.join(
        f'<tr><td style="text-align:center"><b>{k}</b></td>'
        f'<td>{H.escape(en)}</td><td>{H.escape(vi)}</td></tr>'
        for k, en, vi in FRAMEWORK_MAP)
    fw_table = ('<p class="note"><b>Khung lý thuyết / đối chiếu danh mục '
                '(EN: Halliday &amp; Hasan 1976 — VI: Trần Ngọc Thêm 2006):</b></p>'
                '<table class="framework"><tr><th>Ký hiệu</th>'
                '<th>Tiếng Anh — Halliday &amp; Hasan (1976)</th>'
                '<th>Tiếng Việt — Trần Ngọc Thêm (2006)</th></tr>'
                f'{fw_rows}</table>')
    head = (HTML_CSS
            .replace('__TITLE__', H.escape(DOC_TITLE))
            .replace('__INTRO__', H.escape(INTRO))
            .replace('__LEGEND__', legend))
    return (head + ref_note + fw_table + '\n' + '\n'.join(pair_sections)
            + '\n</body>\n</html>\n')


# ============================================================
# Main build
# ============================================================

def side_ir(raw, ext):
    if raw == 'none':
        return {'kind': 'none'}
    if ext.is_duplicate(raw):
        # The cell text occurred earlier — but if a LATER occurrence carries
        # unconsumed markers (annotated second instance), render that one.
        rng = ext.find_range(raw)
        if rng and ext.markers_in(rng[0], rng[1]):
            saved_sp = ext.search_pos
            ext.search_pos = rng[1]
            segs = ext.segments(rng[0], rng[1])
            if segs:
                return {'kind': 'segs', 'segs': segs}
            ext.search_pos = saved_sp
        return {'kind': 'dup'}
    rng = ext.find_range(raw)
    if rng:
        a, b, off, raw_prefix = rng
        rep = ext.repair_gap(rng, raw)
        ext.search_pos = b
        if rep:
            a2, rp = rep
            segs = ext.segments(a2, b)
            if segs:
                if rp:
                    segs.insert(0, {'t': rp + ' '})
                return {'kind': 'segs', 'segs': segs}
        segs = ext.segments(a, b)
        if segs:
            if raw_prefix:
                segs.insert(0, {'t': raw_prefix + ' '})
            return {'kind': 'segs', 'segs': segs}
    return {'kind': 'raw', 'text': raw}


def _title_match(candidate, title):
    """Loose title equality (prefix or high similarity)."""
    if not candidate or not title or len(candidate) <= 10:
        return False
    if candidate == title or title.startswith(candidate) \
            or candidate.startswith(title):
        return True
    return difflib.SequenceMatcher(None, candidate, title).ratio() >= 0.88


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print('Parsing raw markdown...')
    raw_pairs = parse_raw_file()

    md_out = [f'# {DOC_TITLE}', '', INTRO, '', '**Chú giải màu (Legend):**', '',
              '| Màu | Ký hiệu | Danh mục (Halliday & Hasan 1976 / Trần Ngọc Thêm 2006) |',
              '| :--- | :--- | :--- |']
    for k, c in CATS.items():
        swatch = (f'<span style="background-color:{c["bg"]};color:{c["fg"]};'
                  f'padding:1px 8px;border-radius:3px">&nbsp;{k}&nbsp;</span>')
        md_out.append(f'| {swatch} | {k} {c["emoji"]} | {c["en"]} — {c["vi"]} |')
    md_out += ['',
               '**Hướng tham chiếu (R — A/C/E):** mỗi khối R kèm chữ mũ: '
               '<sup>A</sup> = anaphoric (hồi quy — tiền trạm nằm trước trong '
               'văn bản), <sup>C</sup> = cataphoric (tiến chỉ — tiền trạm nằm '
               'sau), <sup>E</sup> = exophoric (ngoại văn bản — tiền trạm trong '
               'bối cảnh phát ngôn: người viết / độc giả). Toàn ngữ liệu không '
               'có trường hợp C liên-câu. (Chữ mũ <sup>E</sup> này khác ký hiệu '
               'danh mục E = lược bỏ.)',
               '',
               '**Khung lý thuyết / đối chiếu danh mục** (EN: Halliday & Hasan '
               '1976 — VI: Trần Ngọc Thêm 2006, dẫn theo Nguyễn Thanh Tùng '
               '2020):',
               '',
               '| Ký hiệu | Tiếng Anh — Halliday & Hasan (1976) | Tiếng Việt — Trần Ngọc Thêm (2006) |',
               '| :--- | :--- | :--- |']
    for k, en, vi in FRAMEWORK_MAP:
        md_out.append(f'| **{k}** | {en} | {vi} |')
    md_out += ['',
               '> Đối chiếu gần đúng giữa hai khung: phép thế đại từ ≈ reference '
               '+ substitution; phép tỉnh lược ≈ ellipsis; phép nối ≈ '
               'conjunction; phép lặp, phép đối, phép thế đồng nghĩa, phép liên '
               'tưởng ≈ lexical cohesion.',
               '', MD_NOTE, '']

    html_sections = []
    all_pairs_ir = []
    stats = {}
    issues = []
    grand = {'en_markers': 0, 'en_rendered': 0, 'vi_markers': 0, 'vi_rendered': 0,
             'en_straddle': 0, 'vi_straddle': 0, 'en_orphan': 0, 'vi_orphan': 0,
             'en_deferred': 0, 'vi_deferred': 0}

    for pair_num in range(1, 21):
        pair_id = f'P{pair_num:02d}'
        raw = raw_pairs[pair_id]
        with open(os.path.join(PAIRS_DIR, pair_id, 'meta.json'), 'r',
                  encoding='utf-8') as f:
            meta = json.load(f)

        title_en_norm = normalize_for_match(meta.get('title_en', ''))
        title_vi_norm = normalize_for_match(meta.get('title_vi', ''))
        filtered_rows = []
        for en_raw, vi_raw in raw['rows']:
            en_n = normalize_for_match(en_raw) if en_raw != 'none' else ''
            vi_n = normalize_for_match(vi_raw) if vi_raw != 'none' else ''
            en_is_title = len(en_n) > 10 and _title_match(en_n, title_en_norm)
            vi_is_title = len(vi_n) > 10 and _title_match(vi_n, title_vi_norm)
            if en_is_title and vi_is_title:
                continue
            if (en_is_title and vi_raw == 'none') or \
                    (vi_is_title and en_raw == 'none'):
                continue
            filtered_rows.append((en_raw, vi_raw))

        st_ext = HighlightExtractor(os.path.join(PAIRS_DIR, pair_id,
                                                 'ST_highlighted.md'),
                                    pair_id, 'ST')
        tt_ext = HighlightExtractor(os.path.join(PAIRS_DIR, pair_id,
                                                 'TT_highlighted.md'),
                                    pair_id, 'TT')

        rows_ir = []
        for en_raw, vi_raw in filtered_rows:
            en_side = side_ir(en_raw, st_ext)
            vi_side = side_ir(vi_raw, tt_ext)
            if en_side['kind'] == 'dup' and vi_side['kind'] == 'dup':
                continue
            if (en_side['kind'] == 'dup' and vi_raw == 'none') or \
                    (vi_side['kind'] == 'dup' and en_raw == 'none'):
                continue
            rows_ir.append({'en': en_side, 'vi': vi_side})

        total_en = sum(1 for r in rows_ir if r['en']['kind'] != 'none')
        total_vi = sum(1 for r in rows_ir if r['vi']['kind'] != 'none')
        en_match = sum(1 for r in rows_ir if r['en']['kind'] == 'segs')
        vi_match = sum(1 for r in rows_ir if r['vi']['kind'] == 'segs')

        stats[pair_id] = {
            'rows': len(rows_ir),
            'en_total': total_en, 'en_matched': en_match,
            'vi_total': total_vi, 'vi_matched': vi_match,
            'en_markers': len(st_ext.markers), 'en_rendered': st_ext.rendered,
            'en_rendered_by_cat': st_ext.rendered_by_cat,
            'vi_markers': len(tt_ext.markers), 'vi_rendered': tt_ext.rendered,
            'vi_rendered_by_cat': tt_ext.rendered_by_cat,
            'straddles': st_ext.straddles + tt_ext.straddles,
            'orphan_markers': st_ext.orphan_markers + tt_ext.orphan_markers,
            'deferred': st_ext.deferred + tt_ext.deferred,
        }
        grand['en_markers'] += len(st_ext.markers)
        grand['en_rendered'] += st_ext.rendered
        grand['vi_markers'] += len(tt_ext.markers)
        grand['vi_rendered'] += tt_ext.rendered
        grand['en_straddle'] += st_ext.straddles
        grand['vi_straddle'] += tt_ext.straddles
        grand['en_orphan'] += st_ext.orphan_markers
        grand['vi_orphan'] += tt_ext.orphan_markers
        grand['en_deferred'] += st_ext.deferred
        grand['vi_deferred'] += tt_ext.deferred

        if en_match < total_en * 0.8 or vi_match < total_vi * 0.8:
            issues.append(f'{pair_id}: EN {en_match}/{total_en}, '
                          f'VI {vi_match}/{total_vi}')
        print(f'  {pair_id}: rows {len(rows_ir)} | EN segs {en_match}/{total_en}, '
              f'markers {st_ext.rendered}/{len(st_ext.markers)} | '
              f'VI segs {vi_match}/{total_vi}, '
              f'markers {tt_ext.rendered}/{len(tt_ext.markers)}'
              + (f' | STRADDLE {st_ext.straddles + tt_ext.straddles}'
                 if st_ext.straddles + tt_ext.straddles else '')
              + (f' | ORPHAN {st_ext.orphan_markers + tt_ext.orphan_markers}'
                 if st_ext.orphan_markers + tt_ext.orphan_markers else ''))

        # ---- markdown ----
        md_out.append(f'## Pair {pair_num:02d}')
        md_out.append('')
        en_url = raw['en_url'] or ''
        vi_url = raw['vi_url'] or ''
        en_header = f'[EN]({en_url})' if en_url else 'EN'
        vi_header = f'[VI]({vi_url})' if vi_url else 'VI'
        md_out.append(f'| {en_header} | {vi_header} |')
        md_out.append('| :--- | :--- |')
        title_en = meta.get('title_en', '')
        title_vi = meta.get('title_vi', '')
        if title_en or title_vi:
            md_out.append(f'| **{title_en.replace("|", "\\\\|")}** | '
                          f'**{title_vi.replace("|", "\\\\|")}** |')
        for r in rows_ir:
            en_cell = md_side(r['en'])
            vi_cell = md_side(r['vi'])
            if en_cell or vi_cell:
                md_out.append(f'| {en_cell} | {vi_cell} |')
        md_out.append('')

        # ---- html ----
        en_th = f'<a href="{H.escape(en_url, quote=True)}">EN</a>' if en_url else 'EN'
        vi_th = f'<a href="{H.escape(vi_url, quote=True)}">VI</a>' if vi_url else 'VI'
        h = [f'<h2 id="{pair_id}">Pair {pair_num:02d}</h2>', '<table>',
             f'<tr><th>{en_th}</th><th>{vi_th}</th></tr>']
        if title_en or title_vi:
            h.append(f'<tr class="titles"><td><b>{H.escape(title_en)}</b></td>'
                     f'<td><b>{H.escape(title_vi)}</b></td></tr>')
        for r in rows_ir:
            h.append(f'<tr><td>{html_side(r["en"])}</td>'
                     f'<td>{html_side(r["vi"])}</td></tr>')
        h.append('</table>')
        html_sections.append('\n'.join(h))

        # ---- IR ----
        all_pairs_ir.append({
            'id': pair_id, 'num': pair_num,
            'en_url': en_url, 'vi_url': vi_url,
            'title_en': title_en, 'title_vi': title_vi,
            'rows': rows_ir,
        })

    # ---- write outputs ----
    md_path = os.path.join(OUT_DIR, 'Appendix1.md')
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_out) + '\n')

    html_path = os.path.join(OUT_DIR, 'Appendix1.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(build_html_doc(html_sections))

    ir = {
        'title': DOC_TITLE, 'intro': INTRO,
        'cats': {k: {'bg': c['bg'], 'fg': c['fg'], 'en': c['en'], 'vi': c['vi']}
                 for k, c in CATS.items()},
        'ref_names': REF_NAMES,
        'framework_map': [
            {'key': k, 'en': en, 'vi': vi} for k, en, vi in FRAMEWORK_MAP],
        'totals': grand,
        'pairs': all_pairs_ir,
    }
    ir_path = os.path.join(OUT_DIR, 'appendix1_segments.json')
    with open(ir_path, 'w', encoding='utf-8') as f:
        json.dump(ir, f, ensure_ascii=False)

    with open(os.path.join(OUT_DIR, 'match_stats.json'), 'w', encoding='utf-8') as f:
        json.dump({'grand': grand, 'pairs': stats}, f, ensure_ascii=False, indent=2)

    print(f'\nOutput: {md_path} ({os.path.getsize(md_path)} bytes)')
    print(f'Output: {html_path} ({os.path.getsize(html_path)} bytes)')
    print(f'Output: {ir_path} ({os.path.getsize(ir_path)} bytes)')
    print(f"\nMarker coverage: EN {grand['en_rendered']}/{grand['en_markers']} "
          f"({100 * grand['en_rendered'] / max(1, grand['en_markers']):.1f}%), "
          f"VI {grand['vi_rendered']}/{grand['vi_markers']} "
          f"({100 * grand['vi_rendered'] / max(1, grand['vi_markers']):.1f}%)")
    print(f"Straddles: {grand['en_straddle'] + grand['vi_straddle']}, "
          f"orphans: {grand['en_orphan'] + grand['vi_orphan']}, "
          f"deferred: {grand['en_deferred'] + grand['vi_deferred']}")
    if issues:
        print('\nPairs with low ROW match rates (markers may be missing there):')
        for iss in issues:
            print(f'  {iss}')


if __name__ == '__main__':
    main()
