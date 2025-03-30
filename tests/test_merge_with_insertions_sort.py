from Recursive_insert_merge_sort import recurse_insert_merge_sort
import pytest
import random

def test_reversed_array():
    array = [234, 233, 206, 200, 197, -45, -355, -1423]
    assert recurse_insert_merge_sort(array) == sorted(array)

def test_sorted_array():
    array = [4, 8, 9, 45, 46, 78, 99, 199]
    assert recurse_insert_merge_sort(array) == array

def test_with_doubles_array():
    array = [5, -7, -5, 9, 908, 65, 45, 3, -7]
    assert recurse_insert_merge_sort(array) == sorted(array)

def test_random_array():
    array = []
    for i in range(10):
        array.append(random.randint(-1000, 1000))
    assert recurse_insert_merge_sort(array) == sorted(array)

def test_incorrect_array():
    array = [4, 4, "9", 11, -6, -34, 3, 9]
    with pytest.raises(TypeError):
        recurse_insert_merge_sort(array)