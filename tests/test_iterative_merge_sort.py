from Iterative_merge_sort import iterative_merge_sort
import pytest
import random

def test_reversed_array():
    array = [1900, 590, 587, 32, 0, -34, -35, -67, -2780]
    assert iterative_merge_sort(array) == sorted(array)

def test_sorted_array():
    array = [-200, -45, -7, -4, 0, 12, 19, 2123]
    assert iterative_merge_sort(array) == array

def test_with_doubles_array():
    array = [4, 6, 8, 8, -12, -2, 6, 57]
    assert iterative_merge_sort(array) == sorted(array)

def test_random_array():
    array = []
    for i in range(10):
        array.append(random.randint(-1000, 1000))
    assert iterative_merge_sort(array) == sorted(array)

def test_incorrect_array():
    array = [4, 8, 9, 5, 78, "8", "5", 6, -4, 9, 79]
    with pytest.raises(TypeError):
        iterative_merge_sort(array)