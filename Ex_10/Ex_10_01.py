# Open the file, make a dictionary than split by words, counting words from(each new one starts with zero)
documents = None

while documents == None:
    adddoc = input('Enter File:')
    try:
        documents = open(adddoc)
    except:
        print('file not found')


counts = dict()
for line in documents:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        # if word not in counts:
        #     counts[word] = 1
        # else:
        #     counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst = sorted(lst, reverse=True)

# lst.sort(reverse=True)
# Print the first 10 words by Value first instead of key
for key, val in lst[:10]:
    print(key, val)
