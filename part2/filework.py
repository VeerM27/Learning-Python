# mbox-short = /Users/xeves/Documents/PDA/part2/mbox-short.txt
# mbox = /Users/xeves/Documents/PDA/part2/mbox.txt
# text = /Users/xeves/Documents/PDA/part2/text.txt

fname = input('Enter filename: ')

try:
    fhand = open(fname)
except :
    print('File not found!')
    quit()

count = 0
content = fhand.read()
for line in fhand :
    count += 1

print(count)
