counts = dict()
fname = input('Enter filename: ')

try:
    fhand = open(fname)
except :
    print('File not found!')
    quit()

for line in fhand :
    line = line.rstrip()
    words = line.split()

for word in words :
    counts[word] = counts.get(word, 0) + 1

bigWord = None
bigCount = None
for word,count in counts.items() :
    if bigCount is None or count > bigCount :
        bigWord = word
        bigCount = count

print(counts)
print('\nCounting...')
print('\nThe most common word is:', bigWord, 'with', bigCount, 'occurrences.')
