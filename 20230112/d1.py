import itertools


def calc_cumulative_sum(arr):
    """
    累積和を求める
    Parameters
    ----------
    arr : int[]
        累積和を求めたい配列
    Returns
    -------
    arr : int[]
        累積和の配列
    """
    return list(itertools.accumulate(arr))


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    ans = 0
    for i in range(N):
        ans += A[i]*i - A[i]*(N - 1 - i)
        print(ans)
    print(ans)

    diff = []
    for i in range(N - 1):
        diff.append(A[i + 1] - A[i])
    print(diff)

    s = calc_cumulative_sum(A)
    print(s)
    print(sum(s))

    # ans = 0
    # for i in range(len(diff)):
    #     ans += diff[i] * abs((i + 1) - N) + diff[i] * abs(N - (i + 1))

    # print(ans)


if __name__ == "__main__":
    main()
