def main():
    H, W = map(int, input().split())
    # M行1列のデータ入力
    S = [input() for _ in range(H)]
    # print(S)

    k = [[0 for j in range(2)] for i in range(2)]
    flag = False
    # コマのindexを調べる
    for h in range(H):
        for w in range(W):
            s = S[h][w]
            if s == 'o':
                # print(h, w)
                if not flag:
                    k[0][0] = h
                    k[0][1] = w
                    flag = True
                else:
                    k[1][0] = h
                    k[1][1] = w

    count = 0
    # print(k)
    count += abs(k[0][0] - k[1][0])
    count += abs(k[0][1] - k[1][1])
    print(count)


if __name__ == "__main__":
    main()
