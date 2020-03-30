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
