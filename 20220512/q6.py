import itertools


def main():
    # 1行複数列のデータ入力
    l = list(map(int, input().split()))

    sumC = 0
    for i in range(len(l)):
        sumC += l[i]
    # print('sumC', sumC)
    sumNow = 0
    for i in range(1, 4):
        # i個取る
        nowComb = list(itertools.combinations(range(4), i))
        for c in nowComb:
            # print('c', c)
            for n in range(i):
                # print('n', n)
                # print(l[c[n]], 'を取ります')
                sumNow += l[c[n]]
            # print('sumNow', sumNow)
            if sumNow == sumC / 2:
                print('Yes')
                exit()
            sumNow = 0
        # print(nowComb)
    print('No')


if __name__ == "__main__":
    main()
