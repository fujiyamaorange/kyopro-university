def main():
    s = input()
    s_list = list(s)
    big = False
    small = False
    diff = False

    for i in s_list:
        if i.islower():
            small = True
        elif i.isupper():
            big = True

    s.lower()
    unique_len = len(s)
    set_s_len = len(list(set(s)))
    if (unique_len == set_s_len):
        diff = True

    if (small and big and diff):
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
