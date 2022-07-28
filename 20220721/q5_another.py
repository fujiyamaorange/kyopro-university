N, Q = map(int, input().split())
fll = []
for i in range(N):
    fll.append([0]*N)

for i in range(Q):
    sl = list(map(int, input().split()))
    if sl[0] == 1:
        #		print('sl[0]=',sl[0])
        fll[sl[1]-1][sl[2]-1] = 1
#		print('fll:',fll)
    elif sl[0] == 2:
        for j in range(N):
            if j == sl[1]-1:
                continue
            if fll[j][sl[1]-1] == 1:
                fll[sl[1]-1][j] = 1
    elif sl[0] == 3:
        tmpl = [0]*N
        for k in range(N):
            if k == sl[1]-1:
                continue
            if fll[sl[1]-1][k] == 1:
                for l in range(N):
                    if l == sl[1]-1:
                        continue
                    if fll[k][l] == 1:
                        tmpl[l] = 1
        for l in range(N):
            if tmpl[l] == 1:
                fll[sl[1]-1][l] = 1

for fl in fll:
    for f in fl:
        if f == 1:
            print('Y', sep='', end='')
        else:
            print('N', sep='', end='')
    print('')
