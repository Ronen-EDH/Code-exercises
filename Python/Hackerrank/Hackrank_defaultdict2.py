from collections import defaultdict
n, m = input().split()
d = defaultdict(list)

for i in range(int(n)):
    d[input()].append(str(i+1))

for _ in range(int(m)):
    i = input()
    print(' '.join(d[i])) if d[i] else print(-1)
