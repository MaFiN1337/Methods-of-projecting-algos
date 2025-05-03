def is_reachable_sum(s, c):
    #Часова складність: O(s*c), для кожного числа в сумі s розглядається с монет
    if s >= sum(c):
        return s == sum(c)
    dp = [False for _ in range(s + 1)]
    dp[0] = True
    for coin in c:
        for i in range(s, coin-1, -1):
            if dp[i - coin]:
                dp[i] = True
                if i == s and dp[s]:
                    return True
    return dp[-1]


def main():
    s = int(input("Enter the target sum: "))
    c = [int(x) for x in input("Enter coins nominal separated by comma: ").strip().split(',')]
    print(is_reachable_sum(s, c))

if __name__ == '__main__':
    main()