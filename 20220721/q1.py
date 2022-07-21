def main():
    S = input()
    S_List = list(S)
    # print(S_List)
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for s in S_List:
        if s in alpha:
            print('error')
            exit()
    n = int(S)
    print(n * 2)


if __name__ == "__main__":
    main()
