n, m = map(int, input().split())
a = list(map(int, input().split()))

s = 0
t = 0
for i in range(0, m):
    s += a[i] * (i+1)
    t += a[i]

print('s:', s)
print('t:', t)
maxnum = s
for i in range(0, n-m):

    ns = s + (m*a[i+m]) - t
    nt = t - a[i] + a[i+m]
    print('ns:', ns)
    print('nt:', nt)

    maxnum = max(maxnum, ns)

    s = ns
    t = nt

print(maxnum)
