def main():
    # nのデータ入力
    n = int(input())
    # N行2列のデータ入力
    ab = [map(int, input().split()) for _ in range(n)]
    a, b = [list(i) for i in zip(*ab)]

    count = 0
    for i in reversed(range(0, n)):
        a[i] += count
        amari = a[i] % b[i]

        if amari != 0:
            count += b[i] - amari

    print(count)


if __name__ == "__main__":
    main()
