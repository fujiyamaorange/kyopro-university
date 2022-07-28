def main():
    S = input()
    S_list = list(S)
    # print(S_list)

    words = []
    # 全て小文字にしたもの
    lower_words = []
    count = 0
    word = ''
    # 小文字にしたもの
    lower_word = ''
    for c in S_list:
        word += c
        lower_word += c.lower()
        if c.isupper():
            count += 1
            if count == 2:
                lower_words.append(lower_word)
                words.append([word, lower_word])
                word = ''
                lower_word = ''
                count = 0

    # print(words)
    sorted_words = sorted(words, key=lambda x: x[1])
    # sorted_lower_words = sorted(lower_words)
    # print(sorted_words)
    for word in sorted_words:
        print(word[0], sep='', end='')
    print()
    # print(sorted_lower_words)


if __name__ == "__main__":
    main()
