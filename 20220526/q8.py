def main():
    # n, kのデータ入力
    n, k = map(int, input().split())
    # 1行複数列のデータ入力
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_oishii = -1

    for v in a:
        if v >= max_oishii:
            max_oishii = v

    max_index = []
    for i in range(len(a)):
        if a[i] == max_oishii:
            max_index.append(i + 1)

    for j in b:
        for k in max_index:
            if j == k:
                print('Yes')
                exit()

    print('No')


if __name__ == "__main__":
    main()
