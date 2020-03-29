import bwt_fm_simple as bfs
import bwt_fm_optimized as bfo

def main():

    bwt_fms = [("Simple algorithm", get_bwt_fm_simple), ("Optimized algorithm", get_bwt_fm_optimized)]

    for bwt_fm in bwt_fms:
        print("--------------------------- " + bwt_fm[0] + " ---------------------------")

        print("Testing suffix arrays")
        test_suffix_array(bwt_fm[1], "", [0])
        test_suffix_array(bwt_fm[1], "ABAABA", [6, 5, 2, 3, 0, 4, 1])
        test_suffix_array(bwt_fm[1], "BANANA", [6, 5, 3, 1, 0, 4, 2])
        test_suffix_array(bwt_fm[1], "MAMA", [4, 3, 1, 2, 0])
        test_suffix_array(bwt_fm[1], "ABRACADABRA", [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2])

        print("Testing bwt")
        test_bwt(bwt_fm[1], "", "$")
        test_bwt(bwt_fm[1], "ABAABA", "ABBA$AA")
        test_bwt(bwt_fm[1], "BANANA", "ANNB$AA")
        test_bwt(bwt_fm[1], "MAMA", "AMMA$")
        test_bwt(bwt_fm[1], "ABRACADABRA", "ARD$RCAAAABB")

        print("Testing count per char")
        test_count_per_char(bwt_fm[1], "", {'$' : 1})
        test_count_per_char(bwt_fm[1], "ABAABA", {'A' : 4, 'B' : 2, '$' : 1})
        test_count_per_char(bwt_fm[1], "BANANA", {'A' : 3, 'B' : 1, 'N' : 2, '$' : 1})
        test_count_per_char(bwt_fm[1], "MAMA", {'A' : 2, 'M' : 2, '$' : 1})
        test_count_per_char(bwt_fm[1], "ABRACADABRA", {'A': 5, 'B': 2, 'C': 1, 'D': 1, 'R': 2, '$': 1})

        print("Testing first column")
        test_first_column(bwt_fm[1], "", {'$' : (0, 1)})
        test_first_column(bwt_fm[1], "ABAABA", {'A' : (1, 5), 'B' : (5, 7), '$' : (0, 1)})
        test_first_column(bwt_fm[1], "BANANA", {'A' : (1, 4), 'B' : (4, 5), 'N' : (5, 7), '$' : (0, 1)})
        test_first_column(bwt_fm[1], "MAMA", {'A' : (1, 3), 'M' : (3, 5), '$' : (0, 1)})
        test_first_column(bwt_fm[1], "ABRACADABRA", {'A': (1, 6), 'B': (6, 8), 'C': (8, 9), 'D': (9, 10), 'R': (10, 12), '$': (0, 1)})

    print("--------------------------- Testing done! ---------------------------")

def get_bwt_fm_simple(text):
    return bfs.BwtFmSimple(text)

def get_bwt_fm_optimized(text):
    return bfo.BwtFmOptimized(text)

def test_suffix_array(factory, text, expected):
    bwt_fm = factory(text)
    assert bwt_fm._suffix_array() == expected

def test_bwt(factory, text, expected):
    bwt_fm = factory(text)
    assert bwt_fm._bwt == expected

def test_count_per_char(factory, text, expected):
    bwt_fm = factory(text)
    assert bwt_fm._count_per_char() == expected

def test_first_column(factory, text, expected):
    bwt_fm = factory(text)
    assert bwt_fm._first_column == expected

main()