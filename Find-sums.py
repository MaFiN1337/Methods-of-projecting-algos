def find_needed_sum(arr, S, current_sum = 0, subset=None, result=None):
    if result is None:
        result = []
    if subset is None:
        subset = []
    if current_sum == S:
        return subset
    if current_sum > S or not arr:
        return None
    with_elem = find_needed_sum(arr[1:], S, arr[0] + current_sum, subset + [arr[0]], result)
    if with_elem and (with_elem[0] not in result):
        result.append(with_elem)
    without_elem = find_needed_sum(arr[1:], S, current_sum, subset, result)
    if without_elem and (without_elem[0] not in result):
        result.append(without_elem)
    return result
# How to modify it without using result?
