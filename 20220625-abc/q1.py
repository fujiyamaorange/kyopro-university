def main():
    # j, kのデータ入力
    n, x = map(int, input().split())
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shou = x // n
    amari = x % n
    if amari != 0:
        shou += 1
    print(s[shou - 1])


if __name__ == "__main__":
    main()
