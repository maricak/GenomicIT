from collections import Counter


class BwtFmInterface:
    def __init__(self, text):
        self._text = text + '$'
        self._suffix_array = self._build_suffix_array()
        self._bwt = self._build_bwt()
        self._counts_per_char = self._build_counts_per_char()
        self._first_column = self._build_first_column()

    def _build_suffix_array(self):
        pass

    def _build_bwt(self):
        bwt = [self._text[suffix_start - 1] if suffix_start != 0 else '$' for suffix_start in self._suffix_array]
        return ''.join(bwt)

    def _build_counts_per_char(self):
        return dict(Counter(self._bwt))

    def _build_first_column(self):
        first_column = {}
        total_count = 0
        for c, count in sorted(self._counts_per_char.items()):
            first_column[c] = (total_count, total_count + count)
            total_count += count
        return first_column

    def _get_b_rank(self, bwt_index):
        pass

    def _full_b_rank(self):
        return [self._get_b_rank(i) for i in range(0, len(self._bwt))]

    def _get_first_column_index(self, c, b_rank):
        return self._first_column[c][0] + b_rank

    def _left_mapping(self, bwt_index):
        c = self._bwt[bwt_index]
        b_rank = self._get_b_rank(bwt_index)
        return self._get_first_column_index(c, b_rank)

    def _full_left_mapping(self):
        return [self._left_mapping(i) for i in range(0, len(self._bwt))]

    def _position_in_text(self, first_column_index):
        pass

    def _full_text_positon(self):
        return [self._position_in_text(i) for i in range(0, len(self._bwt))]

    def _find_predecessors_in_range(self, c, range):
        pass