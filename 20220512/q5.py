def main():
    # x, yのデータ入力
    x, y = map(int, input().split())

    for i in range(x + 1):
        turu = i
        kame = x - i
        if turu * 2 + kame * 4 == y:
            print('Yes')
            exit()
    print('No')


if __name__ == "__main__":
    main()
