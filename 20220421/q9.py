def main():
    n = int(input())
    a = list(map(int, input().split()))

    sumAlice = 0
    sumBob = 0
    a.sort(reverse=True)

    for i in range(len(a)):
        if i % 2 == 0:
            sumAlice += a[i]
        else:
            sumBob += a[i]

    print(sumAlice - sumBob)


if __name__ == "__main__":
    main()
