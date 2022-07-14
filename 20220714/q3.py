
def remove_duplicate(S):
    result = []
    pre = S[0]
    count = 0
    for s in S:
        if s == pre:
            count += 1
        else:
            result.append((pre, count))
            # 次の文字にいく
            count = 1
            pre = s

    # 最後の文字を挿入する
    result.append((pre, count))
    return result


def main():
    S = input()
    T = input()

    # 重複する要素を排除
    S = remove_duplicate(S)
    T = remove_duplicate(T)

    if (len(S) != len(T)):
        print('No')
        exit()

    for s, t in zip(S, T):
        # 各文字が等しいかどうか
        if s[0] == t[0]:
            # 等しくできる条件
            if not (s[1] == t[1] or (s[1] < t[1] and s[1] >= 2)):
                print('No')
                exit()
        else:
            print('No')
            exit()

    print('Yes')


if __name__ == "__main__":
    main()
