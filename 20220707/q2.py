def main():
    # Nのデータ入力
    N = int(input())
    A = [list(map(int, list(input()))) for _ in range(N)]

    d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    ans = 0
    for x in range(N):
        for y in range(N):

            for dx, dy in d:
                tmp = 0
                for _ in range(N):
                    tmp = tmp * 10 + A[y][x]
                    y += dy
                    x += dx

                    y %= N
                    x %= N
                # print(ans)
                # print(tmp)
                ans = max(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
