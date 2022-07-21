def main():
    # データ入力
    A, B, C, D, E, F = map(int, input().split())
    a = [A, B, C, D, E, F]
    a.sort()
    print(a[3])


if __name__ == "__main__":
    main()
