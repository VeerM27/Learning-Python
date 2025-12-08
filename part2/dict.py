fname = input('Enter filename: ')

try:
    fhand = open(fname)
except :
    print('File not found!')
    quit()

counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

bigWord = None
bigCount = None
for word,count in counts.items() :
    if bigCount is None or count > bigCount :
        bigWord = word
        bigCount = count

print('\n', counts)
print('\nCounting...')
print('\nThe most common word is:', bigWord, 'with', bigCount, 'occurrences.\n')
