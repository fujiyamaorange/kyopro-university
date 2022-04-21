def main():
    n = int(input())
    s = input().split()
    count = 0
    flag = 0
    while(True):
        for i in range(n):
            num = int(s[i])
            if num % 2 == 1:
                flag = 1
            else:
                s[i] = num / 2
                # print(s)
        if (flag == 1):
            break
        else:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
