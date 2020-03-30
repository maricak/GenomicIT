import bwt_fm_interface as bfi


class BwtFmOptimized(bfi.BwtFmInterface):
    def __init__(self, text, suffix_array_factor, tally_factor):
        super().__init__(text)
        self._suffix_array_factor = suffix_array_factor
        self._tally_factor = tally_factor
        self._suffix_array = self._downsample_suffix_array()
        self._tally = self._build_tally()

    def _build_suffix_array(self):
        suffix_matrix = sorted([(self._text[i:], i) for i in range(len(self._text))])
        return list(map(lambda suffix_index: suffix_index[1], suffix_matrix))

    def _downsample_suffix_array(self):
        return [position for index, position in enumerate(self._suffix_array) if index % self._suffix_array_factor == 0]

    def _build_tally(self):
        current_count = dict()
        tally = dict()
        for c in self._counts_per_char:
            if c != '$':
                current_count[c] = 0
                tally[c] = []
        for i, c in enumerate(self._bwt):
            if c != '$':
                current_count[c] += 1
            if i % self._tally_factor == 0:
                for c in current_count:
                    tally[c].append(current_count[c])
        return tally
