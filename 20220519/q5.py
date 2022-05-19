def main():
    # N, Wのデータ入力
    N, W = map(int, input().split())
    # N行2列のデータ入力
    wv = [map(int, input().split()) for _ in range(N)]
    w, v = [list(i) for i in zip(*wv)]

    # メモ化配列
    # (W + 1) * (N + 1)
    dp = [[0] * N + 1 for _ in range(W+1)]

    dp[0][0] = 0
    # dp[w][n]はw以下の重さでnまで取得範囲に入れたときの最大値
    # 答えはdp[N][W]？

    for j in range(1, W + 1):
        for k in range(1, N + 1):
            # 取得できたら取得したときの最大値
            # dp[j][k] = max()


if __name__ == "__main__":
    main()
