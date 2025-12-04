fname = input('Enter filename: ')

try:
    fhand = open(fname)
except :
    print('File not found!')
    quit()

entries = []

for line in fhand :
    if line.startswith('Author') :
        lines = line.rstrip()
        entries.append(lines)

for i in entries :
    pos = i.find("@")
    print(i[pos+1:])
