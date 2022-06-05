import math


def main():
    # nのデータ入力
    n = int(input())

    # 平方数のリスト
    l = []

    # 使う分だけ
    for i in range(1, n + 1):
        if (math.sqrt(i)).is_integer():
            l.append(i)
    # print(l)

    count = 0
    for i in range(1, n + 1):
        print('i =', i)
        for a in l:
            if a * i > n:
                print('break: a:', a, 'i:', i)
                break
            for b in l:
                if b * i > n:
                    print('break: b:', b, 'i:', i)
                    break
                print('a * i, b * i =', a * i, b * i)
                count += 1

    print(count)


if __name__ == "__main__":
    main()
