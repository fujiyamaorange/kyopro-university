def main():
    # n, kのデータ入力
    n, k = map(int, input().split())
    # 1行複数列のデータ入力
    a = list(map(int, input().split()))

    # k = 1のときはバブルソートで解ける
    if k == 1:
        print('Yes')
        exit()

    sorted_a = sorted(a)

    for i in range(k):
        x = [v for v in sorted_a[i::k]]
        y = [v for v in a[i::k]]
        y.sort()
        if x != y:
            print('No')
            exit()
    print('Yes')


if __name__ == "__main__":
    main()
