def main():
    num = str(input())
    count = 0
    for i in range(3):
        if num[i] == '1':
            count += 1
    print(count)


if __name__ == "__main__":
    main()
