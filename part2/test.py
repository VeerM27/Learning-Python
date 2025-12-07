fname = input('Enter filename: ')

try:
    fhand = open(fname)
except :
    print('File not found!')
    quit()

for line in fhand :
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From' :
        continue
    print(words[1])
