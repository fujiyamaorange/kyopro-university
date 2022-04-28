def main():
    s1 = input()
    s2 = input()
    s3 = input()
    t = input()
    t = list(t)

    all = ''
    for i in t:
        if i == '1':
            all += s1
        elif i == '2':
            all += s2
        else:
            all += s3
    print(all)


if __name__ == "__main__":
    main()
