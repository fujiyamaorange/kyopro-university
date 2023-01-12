import heapq


def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    head = P[:K]
    head.sort()
    print(head[0])
    heapq.heapify(head)

    for i in range(K, N):
        minimum = heapq.heappop(head)
        new_mini = max(minimum, P[i])
        # すでに存在する値との大小を比べる
        heapq.heappush(head, new_mini)
        ans = heapq.heappop(head)
        print(ans)

        # もう一度入れる
        heapq.heappush(head, ans)


if __name__ == "__main__":
    main()
