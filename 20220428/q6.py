def kyori(a, b, c, x):
    q = x // (a + c)
    r = x % (a + c)
    return (q * a + min(a, r)) * b


def main():
    a, b, c, d, e, f, x = map(int, input().split())
    takahashi = kyori(a, b, c, x)
    aoki = kyori(d, e, f, x)

    if takahashi > aoki:
        print('Takahashi')
    elif aoki > takahashi:
        print('Aoki')
    else:
        print('Draw')


if __name__ == "__main__":
    main()
