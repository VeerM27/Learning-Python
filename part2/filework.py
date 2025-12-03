fname = input('Enter filename: ')

try:
    fhand = open(fname)
except :
    print('File not found!')
    quit()

for line in fhand :
    line = line.upper()
    lines = line.rstrip()
    print(lines)
