def main():
    s = list(input())

    if bool(int(s[0])):
        print('No')
        exit()

    # 各列が倒れているかどうか
    first = not bool(int(s[6]))
    second = not bool(int(s[3]))
    third = not bool(int(s[1])) and not bool(int(s[7]))
    forth = not bool(int(s[0])) and not bool(int(s[4]))
    fifth = not bool(int(s[2])) and not bool(int(s[8]))
    sixth = not bool(int(s[5]))
    seventh = not bool(int(s[9]))

    pins = [first, second, third, forth, fifth, sixth, seventh]
    # print(pins)

    flag = False
    second = False
    for state in pins:
        if flag and second and (not state):
            print('Yes')
            exit()
        elif flag and state:
            # セカンドリーチ
            second = True
        elif state:
            # 倒れていたらcontinue
            continue
        else:
            # 倒れていなければリーチ
            flag = True
    print('No')


if __name__ == "__main__":
    main()
