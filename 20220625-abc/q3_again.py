def main():
    # nのデータ入力
    N = int(input())
    # sのデータ入力
    S = input()
    S = list(S)
    # 1行複数列のデータ入力
    W = list(map(int, input().split()))

    data = [[W[i], S[i]] for i in range(N)]

    # 2次元配列を体重でソートする
    data.sort(key=lambda x: x[0])
    # print(data)

    adults = []
    for d in data:
        if d[1] == '1':
            adults.append(d[0])

    # 最初は全て大人と判断するので初期解は大人の人数
    ans = len(adults)

    x = ans
    for i in range(N):
        if data[i][1] == '1':
            # 大人なら一致数は減る
            x -= 1
        else:
            # 子供なら一致数は増える
            x += 1

        if i < N - 1:
            # 境界の前後で同じ体重の場合は判定できないのでパス
            if data[i][0] != data[i + 1][0]:
                ans = max(x, ans)
        else:
            ans = max(x, ans)

    print(ans)


if __name__ == "__main__":
    main()
