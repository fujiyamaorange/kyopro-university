import bisect


def main():
    # nのデータ入力
    N = int(input())
    # sのデータ入力
    S = input()
    # 1行複数列のデータ入力
    W = list(map(int, input().split()))

    children = []
    adults = []

    child_max = 0
    adult_min = 1_000_000_000

    for n in range(N):
        if S[n] == '0':
            # 子供
            children.append(W[n])
            if W[n] >= child_max:
                child_max = W[n]
        else:
            # 大人
            adults.append(W[n])
            if W[n] <= adult_min:
                adult_min = W[n]

    children.sort()
    adults.sort()

    print('children: ', children)
    print('adults: ', adults)

    # どちらかしかいない時はOK
    if len(adults) == 0 or len(children) == 0:
        print(N)
        exit()

    # きれいに分かれている場合もOK
    if adult_min > child_max:
        print(N)
        exit()

    # 大人でchild_maxより軽い人数
    low_adult_count = 0
    for i in range(len(adults)):
        if adults[i] <= child_max:
            low_adult_count += 1

    high_child_count = 0
    # 子供でadult_minより重い人数
    for i in range(len(children)):
        if children[i] >= adult_min:
            high_child_count += 1

    # 外れる人たち
    count = min(low_adult_count, high_child_count)
    print(N - count)

    print('child_max: ', child_max)
    print('adult_min: ', adult_min)

    print('low_adult_count: ', low_adult_count)
    print('high_child_count: ', high_child_count)


if __name__ == "__main__":
    main()
