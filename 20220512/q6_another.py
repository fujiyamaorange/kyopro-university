def main():
    # a, b, c, dのデータ入力
    l = list(map(int, input().split()))

    sumC = 0
    for i in l:
        sumC += i

    n = 4
    for bit in range(2**n):
        sumNow = 0
        for i in range(n):
            # bitにフラグが立っているかどうかを判定
            if bit & (1 << i):
                # フラグが立っていればsumに加算
                sumNow += l[n-1-i]

        if sumNow == sumC / 2:
            print("Yes")
            # プログラムを終了
            exit()

    print("No")


if __name__ == "__main__":
    main()
