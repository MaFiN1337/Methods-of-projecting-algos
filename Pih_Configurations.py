import math
from itertools import combinations

def find_best_configure(filename):
    def read_and_validate_file(user_file, data_dict):
        try:
            with open(user_file, 'r') as file:
                lines = file.readlines()
                if len(lines) < 2:
                    return None
                first_line = tuple(map(int, lines[0].strip().split()))
                if len(first_line) != 3:
                    return None
                k1, k2, k3 = first_line
                second_line = int(lines[1].strip())
                if not 7 > k3 > k2 > k1 > 1:
                    return None
                if sum(first_line) > second_line or second_line > 12 or second_line < 1:
                    return None

                for line in lines[2:second_line+2]:
                    parts = line.strip().split()
                    if len(parts) != 3:
                        return None
                    key = int(parts[0])
                    val1, val2 = float(parts[1]), float(parts[2])
                    if not (0 < val1 < 1) or not (0 < val2 < 1):
                        return None
                    data_dict[key] = (val1, val2)
                return first_line
        except Exception:
            return None

    def find_best_configuration(curr_max_security, data_dict, curr_scheme=[]):
        for comb in combinations(data_dict.keys(), scheme[len(curr_scheme)]):
            curr_scheme.append(set(comb))
            if find_short_circuit_probability(curr_scheme) < curr_max_security[0]:
                curr_scheme.pop()
                continue
            if len(curr_scheme) == len(scheme):
                probability = find_short_circuit_probability(curr_scheme) - find_breakage_probability(curr_scheme)
                if curr_max_security[0] < probability:
                    curr_max_security = probability, curr_scheme.copy()
                curr_scheme.pop()
                continue
            cut_data_dict = {k: v for k, v in data_dict.items() if k not in curr_scheme[-1]}
            curr_max_security = find_best_configuration(curr_max_security, cut_data_dict , curr_scheme)
            curr_scheme.pop()
        return curr_max_security

    def find_short_circuit_probability(scheme_variant: list[set]) -> float:
        probability = 1
        for connection in scheme_variant:
            current_connection_prob = math.prod([data[detail][0] for detail in connection])
            probability *= 1 - current_connection_prob
        return probability

    def find_breakage_probability(scheme_variant: list[set]) -> float:
        probability = 1
        for connection in scheme_variant:
            current_connection_prob = math.prod([1-data[detail][1] for detail in connection])
            probability *= 1 - current_connection_prob
        return probability

    def amount_of_unique_configurations(all_elements_amount):
        k = sum(scheme)
        choose_uniques = math.comb(all_elements_amount, k)
        denominator = 1
        for row in scheme:
            denominator *= math.factorial(row)
        return choose_uniques * math.factorial(k) // denominator

    data = {}
    scheme = read_and_validate_file(filename, data)
    max_security = [0, []]
    return None if scheme is None else (scheme, len(data)
                                          , amount_of_unique_configurations(len(data))
                                          , find_best_configuration(max_security, data))

def main():
    result = find_best_configure('for_configurations.txt')
    if result is not None:
        print(f"Задана структура: {" ".join(map(str, result[0]))}\n"
              f"Кількість різнотипних елементів: {result[1]}\n"
              f"Кількість різних конфігурацій: {result[2]}\n"
              f"Максимальна надійність: {result[3][0]}\n"
              f"Досягнута на конфігурації: \n")
        for s in result[3][1]:
            print(" ".join(str(x) for x in s))
    else:
        print("Something is wrong with input data")

if __name__ == '__main__':
    main()
