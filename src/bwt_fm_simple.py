import bwt_fm_interface as bfi

class BwtFmSimple(bfi.BwtFmInterface):
    def __init__(self, text):
        super().__init__(text)

    def _suffix_array(self):
        suffix_matrix = sorted([(self._text[i:], i) for i in range(len(self._text))])
        return list(map(lambda suffix_index: suffix_index[1], suffix_matrix))