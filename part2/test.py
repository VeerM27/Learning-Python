fname = input('Enter filename: ')

try:
    fhand = open(fname)
except :
    print('File not found!')
    quit()

entries = []

for line in fhand :
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:') :
        words = line.split()
        entries.append(float(words[1]))
    else : 
        continue

total = sum(entries)

print(entries)
[print(total)]
