import math


def calc(x, y):
    kyori = x * x + y * y
    return math.sqrt(kyori)


def main():
    # n, dのデータ入力
    n, d = map(int, input().split())
    # N行2列のデータ入力
    xy = [map(int, input().split()) for _ in range(n)]
    x, y = [list(i) for i in zip(*xy)]

    count = 0
    for i in range(n):
        kyori = calc(x[i], y[i])
        if kyori <= d:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
