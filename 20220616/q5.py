def main():
    # j, kのデータ入力
    X, A, D, N = map(int, input().split())

    end = D * N
    # print(end)
    # S = [A:end:D]
    S = [v for v in range(A, end, D)]
    # print(S)
    minimum = abs(S[0] - X)
    for s in S:
        sabun = abs(s - X)
        print(s, sabun)
        if sabun <= minimum:
            minimum = sabun

    print(minimum)


if __name__ == "__main__":
    main()
