def go(x, y, way):
    if way == 'N':
        return x, y + 1
    elif way == 'E':
        return x + 1, y
    elif way == 'S':
        return x, y - 1
    else:
        return x - 1, y


def spin(way):
    if way == 'N':
        return 'E'
    elif way == 'E':
        return 'S'
    elif way == 'S':
        return 'W'
    else:
        return 'N'


def main():
    # nのデータ入力
    n = int(input())
    t = list(input())

    way = 'E'
    x = 0
    y = 0
    for s in t:
        if s == 'S':
            x, y = go(x, y, way)
        else:
            way = spin(way)

    print(x, y)


if __name__ == "__main__":
    main()
