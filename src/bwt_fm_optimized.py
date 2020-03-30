import bwt_fm_interface as bfi


class BwtFmOptimized(bfi.BwtFmInterface):
    def __init__(self, text, suffix_array_factor):
        super().__init__(text)
        self._suffix_array = self._downsample_suffix_array(suffix_array_factor)

    def _build_suffix_array(self):
        suffix_matrix = sorted([(self._text[i:], i) for i in range(len(self._text))])
        return list(map(lambda suffix_index: suffix_index[1], suffix_matrix))

    def _downsample_suffix_array(self, factor):
        return [position for index, position in enumerate(self._suffix_array) if index % factor == 0]

    def _build_b_rank_and_counts_per_char(self):
        counts = dict()
        ranks = []
        for c in self._bwt:
            if (c not in counts):
                counts[c] = 0
            ranks.append(counts[c])
            counts[c] += 1
        return ranks, counts
