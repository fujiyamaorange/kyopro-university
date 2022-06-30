def main():
    N, K, Q = map(int, input().split())
    # 1行複数列のデータ入力
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))

    for l in L:
        # 左からl番目のコマに対して操作
        koma = A[l - 1]

        if koma >= N or koma + 1 in A:
            # コマが一番右にあるので増やせない or 既に右にコマが置いてあるので増やせない
            continue
        else:
            A[l - 1] += 1

    for a in A:
        print(a, end=' ')
    print()


if __name__ == "__main__":
    main()
