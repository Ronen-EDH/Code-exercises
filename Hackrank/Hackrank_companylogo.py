from collections import defaultdict
d = defaultdict(int)
string = 'aabbbccde'
for letter in string:
    # print(letter)
    d[letter] += 1
print(d)
