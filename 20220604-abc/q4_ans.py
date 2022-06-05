# ABC254D

N = int(input())
# Nを超えない平方数をリストに格納
x = [i ** 2 for i in range(1, N + 1) if i ** 2 <= N]
# print(x)

seen = [0] * (N + 1)
# print(seen)
ans = 0

# 1からNまでについて調べる
for k in range(1, N + 1):
    if seen[k]:
        # print(k, 'は既に調べました')
        continue
    for a in x:
        if k * a > N:
            break
        for b in x:
            if k * b > N:
                break
            ans += 1
            # kは共通なので必ず平方数になる
            # print(f"seenに追加 a({a}) * k({k}) =", a * k)
            # print(f"seenに追加 b({b}) * k({k}) =", b * k)
            seen[a * k] = 1
            seen[b * k] = 1
print(ans)
