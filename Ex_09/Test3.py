d = {'a': 10, 'c': 1, 'b': 22, 'd': 50, 't': 2, 'e': 70}
x = d.items()
print(x)
# y = sorted(d.items())
# print(y)
for k, v in sorted(d.items()):
    print(k, v)
