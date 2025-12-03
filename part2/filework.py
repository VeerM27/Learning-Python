fname = input('Enter filename: ')

try:
    fhand = open(fname)
except :
    print('File not found!')
    quit()

count = 0
for line in fhand :
    count += 1

print(count)

fhand.seek(0)

content = fhand.read()

print(len(content))