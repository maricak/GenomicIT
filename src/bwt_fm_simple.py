import bwt_fm_interface as bfi


class BwtFmSimple(bfi.BwtFmInterface):
    def __init__(self, text):
        super().__init__(text)
        self._b_rank = self._build_b_rank()

    def _build_suffix_array(self):
        suffix_matrix = sorted([(self._text[i:], i) for i in range(len(self._text))])
        return list(map(lambda suffix_index: suffix_index[1], suffix_matrix))

    def _build_b_rank(self):
        counts = dict()
        ranks = []
        for c in self._bwt:
            if (c not in counts):
                counts[c] = 0
            ranks.append(counts[c])
            counts[c] += 1
        return ranks

    def _get_b_rank(self, bwt_index):
        return self._b_rank[bwt_index]

    def _position_in_text(self, first_column_index):
        return self._suffix_array[first_column_index]

    def _find_predecessors_in_range(self, c, start, end):
        try:
            first = start + self._bwt[start:end].index(c)
            last = end - start - self._bwt[end - 1:start - 1:-1].index(c)
        except ValueError:
            return None
        else:
            return (self._left_mapping(first), self._left_mapping(last))
