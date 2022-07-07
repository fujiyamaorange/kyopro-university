def main():
    # Kのデータ入力
    K = int(input())
    if K < 60:
        print(f'21:{str(K).zfill(2)}')
    else:
        print(f'22:{str(K - 60).zfill(2)}')


if __name__ == "__main__":
    main()
