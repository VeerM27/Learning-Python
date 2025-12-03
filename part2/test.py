fname = input('Enter filename: ')

try:
    fhand = open(fname)
except :
    print('File not found!')
    quit()

entries = []

for line in fhand :
    if line.startswith('X-DSPAM-Confidence:') :
        lines = line.rstrip()
        num = lines[20:28]
        entries.append(num)

sum = 0
count = 0

for i in entries :
    j = float(i)
    sum += j
    count += 1

print(sum, count)

#for line in fhand :
 #   lines = line.rstrip()
  #  print(lines)
