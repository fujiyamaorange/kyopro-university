def main():
    n = int(input())
    count = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            yakusu = [j for j in range(1, i+1) if i % j == 0]
            if len(yakusu) == 8:
                count += 1

    print(count)


if __name__ == "__main__":
    main()
