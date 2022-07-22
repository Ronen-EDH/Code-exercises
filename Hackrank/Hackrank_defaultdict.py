n, m = input().split()
groupe_a = []
groupe_b = []
for _ in range(int(n)):
    groupe_a.append(input())
print(groupe_a)
for _ in range(int(m)):
    groupe_b.append(input())
print(groupe_b)
for x in groupe_b:
    match = []
    if x not in groupe_a:
        print('-1')
        continue
    for index, y in enumerate(groupe_a):
        if x == y:
            index += 1
            match.append(str(index))
    print(" ".join(match))
