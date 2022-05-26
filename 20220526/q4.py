def main():
    # nのデータ入力
    n = int(input())
    # n行1列のデータ入力
    P = [int(input()) for _ in range(n)]

    price = 0
    mx = 99
    for p in P:
        if p >= mx:
            mx = p
        price += p

    print(price - (int(mx / 2)))


if __name__ == "__main__":
    main()
