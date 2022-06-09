def main():
    # sのデータ入力
    s = input()
    s = list(s)

    if s[2] == s[3] and s[4] == s[5]:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
