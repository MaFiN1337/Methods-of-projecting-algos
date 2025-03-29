def recurse_merge_sort(arr):
    if len(arr) == 1:
        return arr
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

print(recurse_merge_sort([1,2,3,4,5,6,7,8,9,10]))
print(recurse_merge_sort([5, 3, 7, 1, 8]))
print(recurse_merge_sort([9, 3, 1, 18, 50]))
