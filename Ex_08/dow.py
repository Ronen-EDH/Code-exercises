han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    print(wds)
    if wds == []:
        continue
    if wds[0] != 'From':
        continue
    print(wds[2])
