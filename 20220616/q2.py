def main():
    a, b, c = map(int, input().split())
    if (a <= b and b <= c) or (a >= b and b >= c):
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
