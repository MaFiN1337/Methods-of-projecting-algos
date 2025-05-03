def print_levenstein(output_str, target_str):
    def process_input(s, t):
        if not (isinstance(s, str) and isinstance(t, str) and s.isalpha() and t.isalpha()):
            raise ValueError('Invalid input')
        return s.lower(), t.lower()

    def pos(char_value):
        return ord(char_value) - ord('a') + 1

    def cost_sub(c_s, c_t):
        return abs(pos(c_s) - pos(c_t)) if c_s != c_t else 0

    def cost_del(c):
        return pos(c)

    def cost_ins(c):
        return pos(c)

    def fill_levenstein_table(table, s, t):
        table[0].append(0)
        for i in range(1, len(t)+1):
            table[0].append(table[0][-1] + cost_ins(t[i - 1]))
        for i in range(1, len(s)+1):
            table.append([])
            table[i].append(table[i-1][0] + cost_del(s[i - 1]))
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                cost_replace = table[i - 1][j - 1] + cost_sub(s[i - 1], t[j - 1])
                cost_delete = table[i - 1][j] + cost_del(s[i - 1])
                cost_insert = table[i][j - 1] + cost_ins(t[j - 1])
                table[i].append(min(cost_replace, cost_delete, cost_insert))


    output_str, target_str = process_input(output_str, target_str)
    levenstein_dist = [[]]
    fill_levenstein_table(levenstein_dist, output_str, target_str)
    for row in levenstein_dist:
        for elem in row:
            print(elem, end=' ')
        print("\n")
    print(f"result: {levenstein_dist[-1][-1]}")

def main():
    s = input("Enter the string that needs to be modified: ")
    t = input(f"Enter the string you want to convert {s} into: ")
    print_levenstein(s, t)


if __name__ == '__main__':
    main()