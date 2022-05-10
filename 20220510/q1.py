import math
import itertools


def calc(x1, y1, x2, y2):
    kyori = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    return math.sqrt(kyori)


def main():
    N = int(input())
    xy = [map(int, input().split()) for _ in range(N)]
    x, y = [list(i) for i in zip(*xy)]

    m = 0
    kumi = list(itertools.combinations(range(N), 2))
    for k in kumi:
        m = max(calc(x[k[0]], y[k[0]], x[k[1]], y[k[1]]), m)

    print(m)


if __name__ == "__main__":
    main()
