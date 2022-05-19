def main():
    # a, bのデータ入力
    a, b = map(int, input().split())

    if a >= 13:
        print(b)
    elif a >= 6:
        print(int(b / 2))
    elif a <= 5:
        print(0)


if __name__ == "__main__":
    main()
