import bwt_fm_simple as bfs
import bwt_fm_optimized as bfo


def main():

    test_cases = [
        {
            "bwt_fm": bfs.BwtFmSimple(""),
            "_suffix_array": [0],
            "_bwt": "$",
            "_counts_per_char": {'$': 1},
            "_first_column": {'$': (0, 1)},
            "_b_rank": [0],
            "_full_b_rank_M": [0],
            "_full_left_mapping_M": [0], 
            "_full_text_positon_M": [0]
        },
        {
            "bwt_fm": bfs.BwtFmSimple("ABAABA"),
            "_suffix_array": [6, 5, 2, 3, 0, 4, 1],
            "_bwt": "ABBA$AA",
            "_counts_per_char": {'A': 4, 'B': 2, '$': 1},
            "_first_column": {'A': (1, 5), 'B': (5, 7), '$': (0, 1)},
            "_b_rank": [0, 0, 1, 1, 0, 2, 3],
            "_full_b_rank_M": [0, 0, 1, 1, 0, 2, 3],
            "_full_left_mapping_M": [1, 5, 6, 2, 0, 3, 4],
            "_full_text_positon_M": [6, 5, 2, 3, 0, 4, 1]
        },
        {
            "bwt_fm": bfs.BwtFmSimple("BANANA"),
            "_suffix_array": [6, 5, 3, 1, 0, 4, 2],
            "_bwt": "ANNB$AA",
            "_counts_per_char": {'A': 3, 'B': 1, 'N': 2, '$': 1},
            "_first_column": {'A': (1, 4), 'B': (4, 5), 'N': (5, 7), '$': (0, 1)},
            "_b_rank": [0, 0, 1, 0, 0, 1, 2],
            "_full_b_rank_M": [0, 0, 1, 0, 0, 1, 2],
            "_full_left_mapping_M": [1, 5, 6, 4, 0, 2, 3],
            "_full_text_positon_M": [6, 5, 3, 1, 0, 4, 2]
        },
        {
            "bwt_fm": bfs.BwtFmSimple("MAMA"),
            "_suffix_array": [4, 3, 1, 2, 0],
            "_bwt": "AMMA$",
            "_counts_per_char": {'A': 2, 'M': 2, '$': 1},
            "_first_column": {'A': (1, 3), 'M': (3, 5), '$': (0, 1)},
            "_b_rank": [0, 0, 1, 1, 0],
            "_full_b_rank_M": [0, 0, 1, 1, 0],
            "_full_left_mapping_M": [1, 3, 4, 2, 0],
            "_full_text_positon_M": [4, 3, 1, 2, 0]
        },
        {
            "bwt_fm": bfs.BwtFmSimple("ABRACADABRA"),
            "_suffix_array": [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2],
            "_bwt": "ARD$RCAAAABB",
            "_counts_per_char": {'A': 5, 'B': 2, 'C': 1, 'D': 1, 'R': 2, '$': 1},
            "_first_column": {'A': (1, 6), 'B': (6, 8), 'C': (8, 9), 'D': (9, 10), 'R': (10, 12), '$': (0, 1)},
            "_b_rank": [0, 0, 0, 0, 1, 0, 1, 2, 3, 4, 0, 1],
            "_full_b_rank_M": [0, 0, 0, 0, 1, 0, 1, 2, 3, 4, 0, 1],
            "_full_left_mapping_M": [1, 10, 9, 0, 11, 8, 2, 3, 4, 5, 6, 7],
            "_full_text_positon_M": [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
        },
        {
            "bwt_fm": bfo.BwtFmOptimized("", 2, 2),
            "_suffix_array": [0],
            "_bwt": "$",
            "_counts_per_char": {'$': 1},
            "_first_column": {'$': (0, 1)},
            "_tally": {},
            "_full_left_mapping_M": [0],
            "_full_b_rank_M": [0],
            "_full_text_positon_M": [0]
        },
        {
            "bwt_fm": bfo.BwtFmOptimized("ABAABA", 2, 1),
            "_suffix_array": [6, 2, 0, 1],
            "_bwt": "ABBA$AA",
            "_counts_per_char": {'A': 4, 'B': 2, '$': 1},
            "_first_column": {'A': (1, 5), 'B': (5, 7), '$': (0, 1)},
            "_tally": {'A': [1, 1, 1, 2, 2, 3, 4], 'B': [0, 1, 2, 2, 2, 2, 2]},
            "_full_b_rank_M": [0, 0, 1, 1, 0, 2, 3],
            "_full_left_mapping_M": [1, 5, 6, 2, 0, 3, 4],
            "_full_text_positon_M": [6, 5, 2, 3, 0, 4, 1]
        },
        {
            "bwt_fm": bfo.BwtFmOptimized("BANANA", 2, 2),
            "_suffix_array": [6, 3, 0, 2],
            "_bwt": "ANNB$AA",
            "_counts_per_char": {'A': 3, 'B': 1, 'N': 2, '$': 1},
            "_first_column": {'A': (1, 4), 'B': (4, 5), 'N': (5, 7), '$': (0, 1)},
            "_tally": {'A': [1, 1, 1, 3], 'B': [0, 0, 1, 1], 'N': [0, 2, 2, 2]},
            "_full_b_rank_M": [0, 0, 1, 0, 0, 1, 2],
            "_full_left_mapping_M": [1, 5, 6, 4, 0, 2, 3],
            "_full_text_positon_M": [6, 5, 3, 1, 0, 4, 2]
        },
        {
            "bwt_fm": bfo.BwtFmOptimized("MAMA", 2, 2),
            "_suffix_array": [4, 1, 0],
            "_bwt": "AMMA$",
            "_counts_per_char": {'A': 2, 'M': 2, '$': 1},
            "_first_column": {'A': (1, 3), 'M': (3, 5), '$': (0, 1)},
            "_tally": {'A': [1, 1, 2], 'M': [0, 2, 2]},
            "_full_b_rank_M": [0, 0, 1, 1, 0],
            "_full_left_mapping_M": [1, 3, 4, 2, 0],
            "_full_text_positon_M": [4, 3, 1, 2, 0]
        },
        {
            "bwt_fm": bfo.BwtFmOptimized("ABRACADABRA", 4, 4),
            "_suffix_array": [11, 3, 4],
            "_bwt": "ARD$RCAAAABB",
            "_counts_per_char": {'A': 5, 'B': 2, 'C': 1, 'D': 1, 'R': 2, '$': 1},
            "_first_column": {'A': (1, 6), 'B': (6, 8), 'C': (8, 9), 'D': (9, 10), 'R': (10, 12), '$': (0, 1)},
            "_tally": {'A': [1, 1, 4], 'B': [0, 0, 0], 'C': [0, 0, 1], 'D': [0, 1, 1], 'R': [0, 2, 2]},
            "_full_b_rank_M": [0, 0, 0, 0, 1, 0, 1, 2, 3, 4, 0, 1],
            "_full_left_mapping_M": [1, 10, 9, 0, 11, 8, 2, 3, 4, 5, 6, 7],
            "_full_text_positon_M": [11, 10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]
        }
    ]

    for test_case in test_cases:
        bwt_fm = test_case["bwt_fm"]
        print(str(type(bwt_fm)) + " " + bwt_fm._text)
        for field, expected in filter(lambda x: x[0] != "bwt_fm", test_case.items()):
            actual = getattr(bwt_fm, field) if not field.endswith("_M") else getattr(bwt_fm, field[:-2])()
            assert actual == expected, "type: {}, text: {}, field: {}\n{} <-- expected\n{} <-- actual".format(
                type(bwt_fm), bwt_fm._text, field, expected, actual)

    print("--------------------------- Testing done! ---------------------------")


if __name__ == '__main__':
    main()
