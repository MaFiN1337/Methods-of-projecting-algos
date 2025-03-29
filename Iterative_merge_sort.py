def iterative_merge_sort(arr):
    subset_size = 1
    while subset_size < len(arr):
        left_index = 0
        while left_index < len(arr) - 1:
            middle_index = min(len(arr) - 1, left_index + subset_size - 1)
            right_index = min(len(arr) - 1, left_index + 2 * subset_size - 1)
            left_subset = arr[left_index:middle_index+1]
            right_subset = arr[middle_index+1:right_index+1]
            arr[left_index:right_index+1] = merge(left_subset, right_subset)
            left_index += 2 * subset_size
        subset_size *= 2
    return arr


def merge(left_arr, right_arr):
    result = []
    while left_arr and right_arr:
        if left_arr[0] < right_arr[0]:
            result.append(left_arr[0])
            left_arr = left_arr[1:]
        else:
            result.append(right_arr[0])
            right_arr = right_arr[1:]
    result.extend(left_arr)
    result.extend(right_arr)
    return result

print(iterative_merge_sort([38, 27, 43, 3, 9, 82, 10]))
