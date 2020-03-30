from collections import Counter


class BwtFmInterface:
    def __init__(self, text):
        self._text = text + '$'
        self._suffix_array = self._build_suffix_array()
        self._bwt = self._build_bwt()
        self._b_rank, self._counts_per_char = self._build_b_rank_and_counts_per_char()
        self._first_column = self._build_first_column()

    def _build_suffix_array(self):
        pass

    def _build_bwt(self):
        bwt = [self._text[suffix_start - 1] if suffix_start != 0 else '$' for suffix_start in self._suffix_array]
        return ''.join(bwt)

    def _build_first_column(self):
        first_column = {}
        total_count = 0
        for c, count in sorted(self._counts_per_char.items()):
            first_column[c] = (total_count, total_count + count)
            total_count += count
        return first_column

    def _build_b_rank_and_counts_per_char(self): 
        pass