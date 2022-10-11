def main():
    S, T = input().split()

    if 'B' in S and 'B' in T:
        # 地下 to 地下
        # 数字を取り出す
        s = int(S[1])
        t = int(T[1])
        print(abs(s - t))
    elif 'F' in S and 'F' in T:
        # 地上 to 地上
        # 数字を取り出す
        s = int(S[0])
        t = int(T[0])
        print(abs(s - t))
    else:
        # それ以外
        if 'B' in S:
            # Sが地下
            s = int(S[1])
            t = int(T[0])
            print(s + t - 1)
        else:
            # Tが地下
            s = int(S[0])
            t = int(T[1])
            print(s + t - 1)


if __name__ == "__main__":
    main()
