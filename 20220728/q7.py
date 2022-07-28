def main():
    # Nのデータ入力
    N = int(input())
    # j, kのデータ入力
    j, k = map(int, input().split())
    # 1行複数列のデータ入力
    l = list(map(int, input().split()))
    # M行1列のデータ入力
    M = int(input())
    a = [int(input()) for _ in range(M)]
    # N行2列のデータ入力
    N = int(input())
    xy = [map(int, input().split()) for _ in range(N)]
    x, y = [list(i) for i in zip(*xy)]


if __name__ == "__main__":
    main()
