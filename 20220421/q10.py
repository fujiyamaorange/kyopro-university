def main():
    n = int(input())
    d = [int(input()) for _ in range(n)]

    d.sort(reverse=True)
    count = 0
    top = 101

    for i in d:
        if i < top:
            top = i
            count += 1

    print(count)


if __name__ == "__main__":
    main()
