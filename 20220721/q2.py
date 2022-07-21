def main():
    # Nのデータ入力
    N = int(input())
    A = [int(input()) for _ in range(N)]

    for index, a in enumerate(A):
        if index == 0:
            continue
        diff = abs(a - A[index - 1])
        if a - A[index - 1] > 0:
            print('up', diff)
        elif a - A[index - 1] < 0:
            print('down', diff)
        else:
            print('stay')


if __name__ == "__main__":
    main()
