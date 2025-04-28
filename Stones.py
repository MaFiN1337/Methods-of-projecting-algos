import math

def find_least_operations(n, piles):
    def process_input(piles_amount, piles_list):
        try:
            piles_amount = int(piles_amount)
            piles_list = [int(x) for x in piles_list.split()]
            if not (2 <= piles_amount <= 200000 and len(piles_list) == piles_amount and all(isinstance(x, int) and x > 0 for x in piles_list)):
                raise ValueError
            return piles_amount, piles_list
        except (ValueError, TypeError):
            print("Problems with input")
            return None, None
        except Exception:
            print("Other error was raised. Input may have been correct")
            return None, None

    def least_operations(piles_list):
        needed_squares = len(piles_list) // 2
        temp = piles_list[:]
        for pile in temp:
            if math.sqrt(pile).is_integer():
                piles_list.remove(pile)
                needed_squares -= 1
        if needed_squares < 1:
            return abs(needed_squares)
        result = -1
        while True:
            temp = piles_list[:]
            for pile in temp:
                if needed_squares == 0:
                    return result
                if math.sqrt(pile).is_integer():
                    needed_squares -= 1
                    result += 1
                else:
                    piles_list.extend([pile + 1, pile - 1])
                piles_list.remove(pile)
            result += 1

    n, piles = process_input(n, piles)
    if not n:
        return -1
    return least_operations(piles)


def main():
    n = input("Number af stones: ")
    piles_list = input("Piles: ")
    print(find_least_operations(n, piles_list))

if __name__ == '__main__':
    main()