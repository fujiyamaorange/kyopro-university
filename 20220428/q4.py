def main():
    n = input()
    reverse = n[::-1]
    reverse = list(reverse)
    for i in reverse:
        if i == '6':
            print(9, end='')
        elif i == '9':
            print(6, end='')
        else:
            print(i, end='')


if __name__ == "__main__":
    main()
