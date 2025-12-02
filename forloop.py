numbers = [4, 13, 41, 46, 15, 76, 101, 6, 81, 55]

smallest_num = None
count = 0

for i in numbers :
    if smallest_num is None :
        smallest_num = i
    if i < smallest_num :
        smallest_num = i
    count += 1

print('The smallest number is ', smallest_num)
print(smallest_num, 'was the smallest out of the', count, 'entries.' )
