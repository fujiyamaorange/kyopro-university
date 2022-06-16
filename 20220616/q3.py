import math


def calc(x1, y1, x2, y2):
    # 距離を求める
    l2 = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    return math.sqrt(l2)


def main():
    # n, kのデータ入力
    N, K = map(int, input().split())
    # 1行複数列のデータ入力
    A = list(map(int, input().split()))
    # N行2列のデータ入力
    XY = [map(int, input().split()) for _ in range(N)]
    X, Y = [list(i) for i in zip(*XY)]

    m_list = [[0 for j in range(N)] for i in range(K)]

    k_index = 0
    for a in A:
        a_index = a - 1
        for i in range(N):
            kyori = calc(X[a_index], Y[a_index], X[i], Y[i])
            m_list[k_index][i] = kyori
        k_index += 1

    lm = -1
    for n_i in range(N):
        minimum = 1000_000_000
        for k_i in range(K):
            if m_list[k_i][n_i] <= minimum:
                minimum = m_list[k_i][n_i]
        if minimum >= lm:
            lm = minimum
    print(lm)


if __name__ == "__main__":
    main()
