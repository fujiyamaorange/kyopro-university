def main():
    # xのデータ入力
    x = int(input())

    count = 0
    nokori = 0
    if x >= 500:
        c1000 = x // 500
        nokori = x % 500
        count += c1000 * 1000
    else:
        nokori = x

    c5 = nokori // 5
    count += c5 * 5
    print(count)


if __name__ == "__main__":
    main()
