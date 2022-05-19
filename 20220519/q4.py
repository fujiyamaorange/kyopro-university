def main():
    # nのデータ入力
    n = int(input())
    # 1行複数列のデータ入力
    h = list(map(int, input().split()))

    INF = 1_000_000_000
    dp = [INF] * n

    # 初期値は0
    for i in range(n):
        if i == 0:
            dp[i] = 0
        elif i == 1:
            dp[i] = abs(h[i] - h[i - 1])
        else:
            dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]),
                        dp[i - 2] + abs(h[i] - h[i - 2]))
        # print(i, ': ', dp[i])

    print(dp[-1])


if __name__ == "__main__":
    main()
