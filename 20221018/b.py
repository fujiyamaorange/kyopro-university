def main():
    X, K = map(int, input().split())

    for i in range(K):
        p = 10 ** (i + 1)
        X = int(X / p + 0.5) * p

    print(X)


if __name__ == "__main__":
    main()
