from collections import deque
d = deque()
n = int(input())
for _ in range(n):
    x, *y = input().split()
    if x == 'append':
        d.append(y[0])
    elif x == 'appendleft':
        d.appendleft(y[0])
    elif x == 'pop':
        d.pop()
    elif x == 'popleft':
        d.popleft()
print(" ".join(d))
