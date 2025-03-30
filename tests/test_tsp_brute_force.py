from Tsp_brute_force import brute_force_tsp
import pytest

def test_brute_force_tsp():
    matrix_4 = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    assert brute_force_tsp(matrix_4) == ([1, 2, 4, 3], 80)

    matrix_5 = [
        [0, 10, 8, 9, 7],
        [10, 0, 10, 5, 6],
        [8, 10, 0, 8, 9],
        [9, 5, 8, 0, 6],
        [7, 6, 9, 6, 0]
    ]
    assert brute_force_tsp(matrix_5) == ([1, 3, 4, 2, 5], 34)

    matrix_6 = [
        [0, 10, 12, 11, 14, 10],
        [10, 0, 13, 15, 8, 12],
        [12, 13, 0, 9, 14, 10],
        [11, 15, 9, 0, 10, 8],
        [14, 8, 14, 10, 0, 6],
        [10, 12, 10, 8, 6, 0]
    ]
    assert brute_force_tsp(matrix_6) == ([1, 2, 5, 6, 4, 3], 53)