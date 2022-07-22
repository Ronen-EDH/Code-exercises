file = open('mbox-short.txt')
# print(file)
for line in file:
    line = line.rstrip()
    print(line.upper())
