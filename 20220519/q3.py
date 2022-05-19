def main():
    # nのデータ入力
    n = int(input())
    # a, b, cをそれぞれindex0, 1, 2に対応させる
    dp = [[0]*3 for _ in range(n+1)]

    # N行3列のデータ入力
    abc = [map(int, input().split()) for _ in range(n)]
    a, b, c = [list(i) for i in zip(*abc)]

    # 0日目の幸福度はa, b, c共に0
    dp[0][0] = 0
    dp[0][1] = 0
    dp[0][2] = 0

    for i in range(1, n + 1):
        now_a = a[i - 1]
        now_b = b[i - 1]
        now_c = c[i - 1]
        dp[i][0] = max(dp[i - 1][1] + now_a, dp[i - 1][2] + now_a)
        dp[i][1] = max(dp[i - 1][0] + now_b, dp[i - 1][2] + now_b)
        dp[i][2] = max(dp[i - 1][0] + now_c, dp[i - 1][1] + now_c)

    # 最終日にどれを取れば最大化されるか
    print(max(dp[-1]))


if __name__ == "__main__":
    main()
