from collections import deque


def main():
    # sのデータ入力
    s = input()
    s = list(s)

    # スタックを定義
    d = deque([])

    for str in s:
        if str >= '0' and str <= '9':
            d.append(int(str))
        else:
            a = d.pop()
            b = d.pop()
            print('a: ', a, 'b: ', b)
            if str == '+':
                d.append(b + a)
            elif str == '-':
                d.append(b - a)
            elif str == '*':
                d.append(b * a)
            else:
                d.append(b / a)

    print('答え: ', d.pop())


if __name__ == "__main__":
    main()
