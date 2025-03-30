import random
from Recursive_merge_sort import recurse_merge_sort
import pytest

def test_reversed_array():
    array = [900, 18, 15, 13, 4, -40, -146, -359, -3890]
    assert recurse_merge_sort(array) == sorted(array)

def test_sorted_array():
    array = [-400, 43, 189, 190, 191, 500, 505, 550, 600]
    assert recurse_merge_sort(array) == array

def test_with_doubles_array():
    array = [3, 65, 2, 7, 3, 8, 21, -300, 66, 65, 876]
    assert recurse_merge_sort(array) == sorted(array)

def test_random_array():
    array = []
    for i in range(10):
        array.append(random.randint(-1000, 1000))
    assert recurse_merge_sort(array) == sorted(array)

def test_incorrect_array():
    array = [4, 8, 9, "5", 10, -6, -34, 93, -9]
    with pytest.raises(TypeError):
        recurse_merge_sort(array)