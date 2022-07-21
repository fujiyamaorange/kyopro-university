def main():
    N, Q = map(int, input().split())
    S = [input() for _ in range(Q)]

    F = [['N' for _ in range(N)] for _ in range(N)]

    for s in S:
        # 各操作を処理していく
        s = s.split(' ')
        if s[0] == '1':
            # 単純にフォローするだけ
            F[int(s[1]) - 1][int(s[2]) - 1] = 'Y'
        elif s[0] == '2':
            # フォロー全返し
            for i in range(N):
                if F[i][int(s[1]) - 1] == 'Y':
                    # フォローし返す
                    F[int(s[1]) - 1][i] = 'Y'
        else:
            # フォローフォロー→フォローしている人のフォローしている人をフォローする
            follow = []
            for i in range(N):
                if F[int(s[1]) - 1][i] == 'Y':
                    follow.append(i)
            for user in follow:
                for i in range(N):
                    if F[user][i] == 'Y':
                        # 自分もフォローする
                        F[int(s[1]) - 1][i] = 'Y'

    for i in range(N):
        for j in range(N):
            print(F[i][j], end='')
        print()


if __name__ == "__main__":
    main()
