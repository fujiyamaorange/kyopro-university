def main():
    a = int(input())  # 500円
    b = int(input())  # 100円
    c = int(input())  # 50円
    x = int(input())

    count = 0
    for i in range(a + 1):
        for j in range(b + 1):
            for k in range(c + 1):
                goukei = 500 * i + 100 * j + 50 * k
                if goukei == x:
                    count += 1

    print(count)


if __name__ == "__main__":
    main()
