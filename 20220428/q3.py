def main():
    a, b = map(int, input().split())
    cover = b * 2
    if cover >= a:
        print(0)
    else:
        print(a - cover)


if __name__ == "__main__":
    main()
