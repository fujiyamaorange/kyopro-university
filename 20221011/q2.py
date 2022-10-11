import collections


def main():
    S = input()
    # print(S)

    count_a = 0
    count_b = 0
    count_c = 0

    for s in S:
        if s == 'a':
            count_a += 1
        elif s == 'b':
            count_b += 1
        else:
            count_c += 1

    # print(max(count_a, count_b, count_c))

    c = collections.Counter(S)
    print(c.most_common()[0][0])


if __name__ == "__main__":
    main()
