import bwt_fm_simple as bfs
import bwt_fm_optimized as bfo


def main():

    bwt_fms = {
        "simple": {
            "empty_string": {
                "bwt_fm": bfs.BwtFmSimple(""),
                "suffix_array": [0],
                "bwt": "$",
                "count_per_char": {'$': 1},
                "first_column": {'$': (0, 1)},
                "b_rank": [0]
            },
            "ABAABA": {
                "bwt_fm": bfs.BwtFmSimple("ABAABA"),
                "suffix_array": [6, 5, 2, 3, 0, 4, 1],
                "bwt": "ABBA$AA",
                "count_per_char": {'A': 4, 'B': 2, '$': 1},
                "first_column": {'A': (1, 5), 'B': (5, 7), '$': (0, 1)},
                "b_rank": [0, 0, 1, 1, 0, 2, 3]
            },
            "BANANA": {
                "bwt_fm": bfs.BwtFmSimple("BANANA"),
                "suffix_array": [6, 5, 3, 1, 0, 4, 2],
                "bwt": "ANNB$AA",
                "count_per_char": {'A': 3, 'B': 1, 'N': 2, '$': 1},
                "first_column": {'A': (1, 4), 'B': (4, 5), 'N': (5, 7), '$': (0, 1)},
                "b_rank": [0, 0, 1, 0, 0, 1, 2]
            },
            "MAMA": {
                "bwt_fm": bfs.BwtFmSimple("MAMA"),
                "suffix_array": [4, 3, 1, 2, 0],
                "bwt": "AMMA$",
                "count_per_char": {'A': 2, 'M': 2, '$': 1},
                "first_column": {'A': (1, 3), 'M': (3, 5), '$': (0, 1)},
                "b_rank": [0, 0, 1, 1, 0]
            },
            "ABRACADABRA": {
                "bwt_fm": bfs.BwtFmSimple("ABRACADABRA"),
                "suffix_array": [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2],
                "bwt": "ARD$RCAAAABB",
                "count_per_char": {'A': 5, 'B': 2, 'C': 1, 'D': 1, 'R': 2, '$': 1},
                "first_column": {'A': (1, 6), 'B': (6, 8), 'C': (8, 9), 'D': (9, 10), 'R': (10, 12), '$': (0, 1)},
                "b_rank": [0, 0, 0, 0, 1, 0, 1, 2, 3, 4, 0, 1]
            }
        },
        "optimized": {
            "empty_string": {
                "bwt_fm": bfo.BwtFmOptimized("", 2),
                "suffix_array": [0],
                "bwt": "$",
                "count_per_char": {'$': 1},
                "first_column": {'$': (0, 1)},
                "b_rank": [0]
            },
            "ABAABA": {
                "bwt_fm": bfo.BwtFmOptimized("ABAABA", 2),
                "suffix_array": [6, 2, 0, 1],
                "bwt": "ABBA$AA",
                "count_per_char": {'A': 4, 'B': 2, '$': 1},
                "first_column": {'A': (1, 5), 'B': (5, 7), '$': (0, 1)},
                "b_rank": [0, 0, 1, 1, 0, 2, 3]
            },
            "BANANA": {
                "bwt_fm": bfo.BwtFmOptimized("BANANA", 2),
                "suffix_array": [6, 3, 0, 2],
                "bwt": "ANNB$AA",
                "count_per_char": {'A': 3, 'B': 1, 'N': 2, '$': 1},
                "first_column": {'A': (1, 4), 'B': (4, 5), 'N': (5, 7), '$': (0, 1)},
                "b_rank": [0, 0, 1, 0, 0, 1, 2]
            },
            "MAMA": {
                "bwt_fm": bfo.BwtFmOptimized("MAMA", 2),
                "suffix_array": [4, 1, 0],
                "bwt": "AMMA$",
                "count_per_char": {'A': 2, 'M': 2, '$': 1},
                "first_column": {'A': (1, 3), 'M': (3, 5), '$': (0, 1)},
                "b_rank": [0, 0, 1, 1, 0]
            },
            "ABRACADABRA": {
                "bwt_fm": bfo.BwtFmOptimized("ABRACADABRA", 2),
                "suffix_array": [11, 7, 3, 8, 4, 9],
                "bwt": "ARD$RCAAAABB",
                "count_per_char": {'A': 5, 'B': 2, 'C': 1, 'D': 1, 'R': 2, '$': 1},
                "first_column": {'A': (1, 6), 'B': (6, 8), 'C': (8, 9), 'D': (9, 10), 'R': (10, 12), '$': (0, 1)},
                "b_rank": [0, 0, 0, 0, 1, 0, 1, 2, 3, 4, 0, 1]
            }
        }
    }

    for algorithm in ["simple", "optimized"]:
        print("--------------------------- " + algorithm + " ---------------------------")

        print("Testing suffix array build")
        for (text, data) in bwt_fms[algorithm].items():
            assert data["bwt_fm"]._suffix_array == data["suffix_array"]

        print("Testing bwt build")
        for (text, data) in bwt_fms[algorithm].items():
            assert data["bwt_fm"]._bwt == data["bwt"]

        print("Testing counts per char")
        for (text, data) in bwt_fms[algorithm].items():
            assert data["bwt_fm"]._counts_per_char == data["count_per_char"]

        print("Testing B-ranks build")
        for (text, data) in bwt_fms[algorithm].items():
            assert data["bwt_fm"]._counts_per_char == data["count_per_char"]

        print("Testing first column")
        for (text, data) in bwt_fms[algorithm].items():
            assert data["bwt_fm"]._b_rank == data["b_rank"]

    print("--------------------------- Testing done! ---------------------------")


if __name__ == '__main__':
    main()
