def main():
    # h, wのデータ入力
    h, w = map(int, input().split())
    # r, cのデータ入力
    r, c = map(int, input().split())

    count = 0
    if c > 1:
        count += 1
    if c < w:
        count += 1
    if r > 1:
        count += 1
    if r < h:
        count += 1
    print(count)


if __name__ == "__main__":
    main()
