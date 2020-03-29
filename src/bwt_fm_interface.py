from collections import Counter

class BwtFmInterface:
    def __init__(self, text):
        self._text = text + '$'
        self._bwt = self._bwt()
        self._first_column = self._first_column()

    def _suffix_array(self):
        pass

    def _bwt(self):
        bwt = []
        for suffix_start in self._suffix_array():
            if suffix_start == 0: bwt.append('$')
            else: bwt.append(self._text[suffix_start - 1])
        return ''.join(bwt)

    def _count_per_char(self):
        return dict(Counter(self._bwt))
       
    def _first_column(self):
        counts = self._count_per_char()
        first_column = {}
        total_count = 0
        for c, count in sorted(counts.items()):
            first_column[c] = (total_count, total_count + count)
            total_count += count
        return first_column
