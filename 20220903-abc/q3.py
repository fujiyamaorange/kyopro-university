import itertools


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(A)
    print(list(itertools.accumulate(A)))

    max_value = -2 * 1000000000

    for i in range(N - M + 1):
        part = A[i:i + M]
        sum = 0
        for i in range(M):
            sum += (i + 1) * part[i]

        if sum >= max_value:
            max_value = sum

        sum = 0

    print(max_value)


if __name__ == "__main__":
    main()
