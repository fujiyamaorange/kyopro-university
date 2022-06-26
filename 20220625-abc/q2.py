def main():
    N, K, Q = map(int, input().split())
    # 1行複数列のデータ入力
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    ANS = [0] * K

    for l in L:
        # 左からl番目のコマに対して操作
        koma = A[l - 1]
        # print('koma', koma)

        if koma >= N:
            # コマが一番右にあるので増やせない
            continue
        elif koma + 1 in A:
            # 既に右にコマが置いてあるので増やせない
            continue
        else:
            A[l - 1] += 1
            # print(A)

    for a in A:
        print(a, end=' ')
    print()


if __name__ == "__main__":
    main()
