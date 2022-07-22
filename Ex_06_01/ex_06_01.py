str = 'X-DSPAM-Confidence: 0.8475 '
firstnum = str.find(':')
print(firstnum)
num = str[firstnum+1:]
num = float(num)
print(num)
