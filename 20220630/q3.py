def main():
    # nのデータ入力
    N = int(input())
    # sのデータ入力
    S = input()
    S = list(S)

    # 1行複数列のデータ入力
    W = list(map(int, input().split()))

    weight_age = [[0 for _ in range(2)] for _ in range(N)]

    for i in range(N):
        weight_age[i][0] = W[i]
        weight_age[i][1] = S[i]

    weight_age.sort(key=lambda x: x[0])
    # print(weight_age)

    # 初期解は大人の人数
    ans = len([v for v in weight_age if v[1] == '1'])

    # 比較する条件は境界線の左右が異なる or 一番右 or 一番左
    x = ans
    for i, v in enumerate(weight_age):
        # print('x', x)
        if weight_age[i][1] == '1':
            x -= 1
            # print('x down: ', x)
        else:
            x += 1
            # print('x up: ', x)

        if i + 1 < len(weight_age):
            if weight_age[i][0] != weight_age[i + 1][0]:
                ans = max(x, ans)
        else:
            ans = max(ans, x)

    print(ans)


if __name__ == "__main__":
    main()
