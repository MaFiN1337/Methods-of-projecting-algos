from itertools import permutations

def calculate_cost(matrix_of_price, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += matrix_of_price[path[i]][path[i + 1]]
    cost += matrix_of_price[path[-1]][path[0]]
    return cost

def brute_force_tsp(matrix_of_price):
    n = len(matrix_of_price)
    cities = list(range(1, n))
    min_curr_cost = float('inf')
    best_curr_path = None
    for perm in permutations(cities):
        path = [0] + list(perm)
        cost = calculate_cost(matrix_of_price, path)
        if cost < min_curr_cost:
            min_curr_cost = cost
            best_curr_path = path
    best_curr_path = [i + 1 for i in best_curr_path]
    return best_curr_path, min_curr_cost
