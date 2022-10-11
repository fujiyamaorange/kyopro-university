def main():
    # nのデータ入力
    # 2 <= N <= 50
    N = int(input())

    S = [list(input().split()) for _ in range(N)]

    for i in reversed(range(0, N - 1)):
        for j in range(1, 2 * N - 2):
            l_c = S[i + 1][0][j - 1]
            c_c = S[i + 1][0][j]
            r_c = S[i + 1][0][j + 1]
            if l_c == 'X' or c_c == 'X' or r_c == 'X':
                if S[i][0][j] == '#':
                    bef = S[i][0][:j]
                    aft = S[i][0][j + 1:]

                    all = bef + 'X' + aft
                    S[i] = [all]

    for i in range(N):
        for j in range(2 * N - 1):
            print(S[i][0][j], end='')
        print()


if __name__ == "__main__":
    main()
