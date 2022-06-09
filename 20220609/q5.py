def main():
    # nのデータ入力
    n = int(input())
    l = [[0 for j in range(n - i)] for i in reversed(range(n))]

    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                l[i][j] = 1
                print('1', end=' ')
            else:
                l[i][j] = l[i - 1][j - 1] + l[i - 1][j]
                print(l[i][j], end=' ')
        print()


if __name__ == "__main__":
    main()
