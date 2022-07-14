import math


def main():
    # abd
    a, b, d = map(int, input().split())

    # ラジアンに変換
    d_rad = math.radians(d)

    a_after = a*math.cos(d_rad)-b*math.sin(d_rad)
    b_after = a*math.sin(d_rad)+b*math.cos(d_rad)

    print(a_after, b_after)


if __name__ == "__main__":
    main()
