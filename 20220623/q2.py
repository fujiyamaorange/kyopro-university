def main():
    # nのデータ入力
    N = int(input())
    # 1行複数列のデータ入力
    A = list(map(int, input().split()))

    p = 0

    # マス目
    l = [0] * 4

    for a in A:

        # pの加算操作
        if a == 1:
            p += l[3]
            l2 = l[2]
            l1 = l[1]
            l[3] = l2
            l[2] = l1
            l[1] = 1
        elif a == 2:
            p += l[2] + l[3]
            l1 = l[1]
            l[3] = l1
            l[2] = 1
            l[1] = 0
        elif a == 3:
            p += l[1] + l[2] + l[3]
            l[3] = 1
            l[2] = 0
            l[1] = 0
        else:
            p += 1 + l[1] + l[2] + l[3]
            l[3] = 0
            l[2] = 0
            l[1] = 0
    print(p)


if __name__ == "__main__":
    main()
