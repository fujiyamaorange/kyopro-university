def digitSum(n):
    # 数値を文字列に変換
    s = str(n)
    # １文字ずつ数値化し配列にする。
    array = list(map(int, s))
    # 合計値を返す
    return sum(array)


def main():
    a, b = map(int, input().split())

    if digitSum(a) >= digitSum(b):
        print(digitSum(a))
    else:
        print(digitSum(b))


if __name__ == "__main__":
    main()
