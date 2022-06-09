def main():
    # a, pのデータ入力
    a, p = map(int, input().split())

    apples = 3 * a + p
    print(apples // 2)


if __name__ == "__main__":
    main()
