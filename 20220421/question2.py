def main():
    n = int(input())]
    count = 0
    if n <= 125:
        count = 4
    if n >= 126 and n <= 211:
        count = 6
    if n >= 212 and n <= 214:
        count = 8
    print(count)


if __name__ == "__main__":
    main()
