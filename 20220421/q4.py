def main():
    a, b = map(int, input().split())
    if a % 2 == 1 and b % 2 == 1:
        print('Odd')
    else:
        print('Even')


if __name__ == "__main__":
    main()
