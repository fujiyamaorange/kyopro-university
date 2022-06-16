def countDiff(s, t):
    count = 0
    if s[0] != t[0]:
        count += 1

    if s[1] != t[1]:
        count += 1

    if s[2] != t[2]:
        count += 1


def main():
    # nのデータ入力
    s = input().split()
    t = input().split()
    # print(s)
    # print(t)
    if countDiff(s, t) == 0:
        print('Yes')
    elif countDiff(s, t) == 2:
        print('No')
    elif countDiff(s, t) == 3:
        print('Yes')


if __name__ == "__main__":
    main()
