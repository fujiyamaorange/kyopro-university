def main():
    # sのデータ入力
    s = input()
    # tのデータ入力
    t = input()

    count = 0
    for i in range(0, len(s)):
        if s[i] != t[i]:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
