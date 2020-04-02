import bwt_fm_interface as bfi
import time


class BwtFmSimple(bfi.BwtFmInterface):
    def __init__(self, text, suffix_array_file=None):
        super().__init__(text, suffix_array_file)

        print("Start building B-rank")
        start = time.time()
        self._b_rank = self._build_b_rank()
        end = time.time()
        print("Done building B-rank in", end - start, "seconds")

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
        if c == '$' or c not in self._counts_per_char:
            return None
        first = last = None
        for i in range(start, end+1):
            if self._bwt[i] == c:
                first = i
                break
        if first == None:
            return None
        for i in range(end, start-1, -1):
            if self._bwt[i] == c:
                last = i
                break
        if last == None:
            return None
        return (self._left_mapping(first), self._left_mapping(last))
