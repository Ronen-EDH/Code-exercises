from collections import defaultdict
d = defaultdict(int)
n = int(input())
for _ in range(n):
    d[input()] += 1
allwords = list(d)

allwords_str = d.values()
listofx = []
for x in allwords_str:
    listofx.append(str(x))
print(len(allwords))
print(" ".join(listofx))

# This line is the same as the above block > print(*d.values()) except print(len(allwords))
