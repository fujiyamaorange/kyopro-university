def main():
    # N行1列のデータ入力
    N = int(input())
    x = 0
    y = 0

    count = [0] * (N + 1)
    for _ in range(N):
        count[int(input())] += 1

    for i in range(1, N+1):
        if count[i] >= 2:
            y = i
        if count[i] == 0:
            x = i
    if x == 0:
        print('Correct')
    else:
        print(y, x)


if __name__ == "__main__":
    main()
