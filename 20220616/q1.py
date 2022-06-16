def main():
    # j, kのデータ入力
    r, c = map(int, input().split())
    a11, a12 = map(int, input().split())
    a21, a22 = map(int, input().split())

    if r == 1:
        if c == 1:
            print(a11)
        else:
            print(a12)
    elif c == 1:
        print(a21)
    else:
        print(a22)


if __name__ == "__main__":
    main()
