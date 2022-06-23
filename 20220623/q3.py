def main():
    # データ入力
    h1, h2, h3, w1, w2, w3 = map(int, input().split())

    # h1 = square[0][0] + square[0][1] + square[0][2]
    # h2 = square[1][0] + square[1][1] + square[1][2]
    # h3 = square[2][0] + square[2][1] + square[2][2]

    # w1 = square[0][0] + square[1][0] + square[2][0]
    # w2 = square[0][1] + square[1][1] + square[2][1]
    # w3 = square[0][2] + square[1][2] + square[2][2]

    count = 0
    # 入る数字は1〜28
    for a in range(1, 29):
        for b in range(1, 29):
            for d in range(1, 29):
                for e in range(1, 29):
                    c = h1 - a - b
                    f = h2 - d - e
                    g = w1 - a - d
                    h = w2 - b - e
                    i = w3 - c - f

                    if(c > 0 and f > 0 and g > 0 and h > 0 and i > 0) and g + h + i == h3:
                        count += 1

    print(count)


if __name__ == "__main__":
    main()
