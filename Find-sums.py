def find_needed_sum(arr, S, current_sum = 0, subset=None):
    if subset is None:
        subset = []
    if current_sum == S:
        return [subset]
    if current_sum > S or not arr:
        return []
    with_elem = find_needed_sum(arr[1:], S, arr[0] + current_sum, subset + [arr[0]])
    without_elem = find_needed_sum(arr[1:], S, current_sum, subset)
    return with_elem + without_elem
