def recurse_insert_merge_sort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) < 7:
        return insert_sort(arr)
    left_side = arr[:len(arr)//2]
    right_side = arr[len(arr)//2:]
    left_arr = recurse_merge_sort(left_side)
    right_arr = recurse_merge_sort(right_side)
    return merge(left_arr, right_arr)

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

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
