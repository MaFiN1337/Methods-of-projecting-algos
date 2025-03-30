import time
import random
import pandas as pd
from Recursive_merge_sort import recurse_merge_sort
from Recursive_insert_merge_sort import recurse_insert_merge_sort

def main():
    reversed_small_arr = [i for i in range(15, 0, -2)]
    reversed_large_arr = [i for i in range(400, -400, -20)]
    sorted_small_arr = [i for i in range(-100, 100, 28)]
    sorted_large_arr = [i for i in range(-1000, 1000, 50)]
    random_small_arr = [random.randint(-900, 900) for _ in range(0, 15, 2)]
    random_large_arr = [random.randint(-1700, 1700) for _ in range(0, 40, 1)]
    with_doubles_small_arr = [random.randint(-1000, 1000) for _ in range(0, 8, 2)]
    with_doubles_small_arr.extend(with_doubles_small_arr)
    with_doubles_large_arr = [random.randint(-1000, 1000) for _ in range(0, 20, 1)]
    with_doubles_large_arr.extend(with_doubles_large_arr)
    results_df = pd.DataFrame({"Reversed Small": [None, None],
                               "Sorted Small": [None, None],
                               "Random Small": [None, None],
                               "With Doubles Small": [None, None],
                               "Reversed Large": [None, None],
                               "Sorted Large": [None, None],
                               "Random Large": [None, None],
                               "With Doubles Large": [None, None]})
    results_df.index = ["Simple merge", "Insert merge"]
    pd.set_option('display.max_columns', None)

    start = time.perf_counter()
    recurse_merge_sort(reversed_small_arr)
    end = time.perf_counter()
    results_df.loc["Simple merge", "Reversed Small"] = end-start
    start = time.perf_counter()
    recurse_insert_merge_sort(reversed_small_arr)
    end = time.perf_counter()
    results_df.loc["Insert merge", "Reversed Small"] = end-start
    start = time.perf_counter()
    recurse_merge_sort(reversed_large_arr)
    end = time.perf_counter()
    results_df.loc["Simple merge", "Reversed Large"] = end-start
    start = time.perf_counter()
    recurse_insert_merge_sort(reversed_large_arr)
    end = time.perf_counter()
    results_df.loc["Insert merge", "Reversed Large"] = end-start
    start = time.perf_counter()
    recurse_merge_sort(sorted_small_arr)
    end = time.perf_counter()
    results_df.loc["Simple merge", "Sorted Small"] = end-start
    start = time.perf_counter()
    recurse_insert_merge_sort(sorted_small_arr)
    end = time.perf_counter()
    results_df.loc["Insert merge", "Sorted Small"] = end - start
    start = time.perf_counter()
    recurse_merge_sort(sorted_large_arr)
    end = time.perf_counter()
    results_df.loc["Simple merge", "Sorted Large"] = end - start
    start = time.perf_counter()
    recurse_insert_merge_sort(sorted_large_arr)
    end = time.perf_counter()
    results_df.loc["Insert merge", "Sorted Large"] = end - start
    start = time.perf_counter()
    recurse_merge_sort(random_small_arr)
    end = time.perf_counter()
    results_df.loc["Simple merge", "Random Small"] = end - start
    start = time.perf_counter()
    recurse_insert_merge_sort(random_small_arr)
    end = time.perf_counter()
    results_df.loc["Insert merge", "Random Small"] = end - start
    start = time.perf_counter()
    recurse_merge_sort(random_large_arr)
    end = time.perf_counter()
    results_df.loc["Simple merge", "Random Large"] = end - start
    start = time.perf_counter()
    recurse_insert_merge_sort(random_large_arr)
    end = time.perf_counter()
    results_df.loc["Insert merge", "Random Large"] = end - start
    start = time.perf_counter()
    recurse_merge_sort(with_doubles_small_arr)
    end = time.perf_counter()
    results_df.loc["Simple merge", "With Doubles Small"] = end - start
    start = time.perf_counter()
    recurse_insert_merge_sort(with_doubles_small_arr)
    end = time.perf_counter()
    results_df.loc["Insert merge", "With Doubles Small"] = end - start
    start = time.perf_counter()
    recurse_merge_sort(with_doubles_large_arr)
    end = time.perf_counter()
    results_df.loc["Simple merge", "With Doubles Large"] = end - start
    start = time.perf_counter()
    recurse_insert_merge_sort(with_doubles_large_arr)
    end = time.perf_counter()
    results_df.loc["Insert merge", "With Doubles Large"] = end - start
    print(results_df)


if __name__ == '__main__':
    main()
