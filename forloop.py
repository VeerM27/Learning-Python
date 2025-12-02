numbers = [4, 13, 41, 46, 15, 76, 101, 6, 81, 55]

largest_num = 0
count = 0

for i in numbers :
    if i > largest_num :
        largest_num = i
    count += 1

print('The largest number is ', largest_num)
print('Number of entries', count)
