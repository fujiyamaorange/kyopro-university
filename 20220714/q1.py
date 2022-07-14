def main():
    # N M X T D
    N, M, X, T, D = map(int, input().split())

    # 生まれたときの身長(A)
    A = T - D * X

    # ax + b
    if M >= X:
        print(T)
    else:
        print(D * M + A)


if __name__ == "__main__":
    main()
