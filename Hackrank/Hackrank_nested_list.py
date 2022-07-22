x = 2
y = 2
z = 2
n = 2

# list = [[xx, yy, zz] for xx in range(x+1) for yy in range(y+1)
# for zz in range(z+1) if xx + yy + zz != n]

list = []

for xx in range(x+1):
    print('x', xx)
    for yy in range(y+1):
        print('y', yy)
        for zz in range(z+1):
            print('z', zz)
            list.append([xx, yy, zz])

print(list)

# for xx in range(x+1):
#     print('x', xx)
#     print(list)
# for yy in range(y+1):
#     print('y', yy)
#     print(list)
# for zz in range(z+1):
#     print('z', zz)
#     list.append([xx, yy, zz])
#     print(list)
