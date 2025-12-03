fname = input('Enter filename: ')

try:
    fhand = open(fname)
except :
    print('File not found!')
    quit()

count = 0
for line in fhand :
    if line.startswith('Subject:') :
        count += 1

print(count)
