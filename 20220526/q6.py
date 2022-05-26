def main():
    # a, b, cのデータ入力
    a, b, c = map(int, input().split())

    if a + b < c:
        # 毒入りのクッキーの方が多い時
        can_eat = a + b  # 美味しい
        print(b + can_eat + 1)  # 最後に毒入りクッキーを食べる
    elif a + b > c:
        # 毒入りのクッキーの方が少ない時
        print(b + c)
    else:
        print(b + c)


if __name__ == "__main__":
    main()
