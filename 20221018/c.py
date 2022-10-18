import collections


def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = [0] * N

    A = sorted(A)
    c = collections.Counter(A)
    # print(c)

    # 重複排除したもの
    sorted_a_sub = sorted(list(set(A)))
    # print(sorted_a_sub)

    for index, a in enumerate(sorted_a_sub):
        # print('c[a]: ', c[a])
        # x種類のxをインデックスに持ってくる
        ans[len(sorted_a_sub) - index - 1] += c[a]

    for n in ans:
        print(n)


if __name__ == "__main__":
    main()
