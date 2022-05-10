def makeString(n):
    if (n == 1):
        return '1'

    dn = n - 1
    s = makeString(dn) + ' ' + str(n) + ' ' + makeString(dn)
    return s


def main():
    # nのデータ入力
    n = int(input())
    print(makeString(n))


if __name__ == "__main__":
    main()
