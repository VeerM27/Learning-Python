numbers = []
sum = 0
count = 0

entry = input('Enter a number: ')

while entry != 'done':
    try:
        num = int(entry)
        numbers.append(num)
    except ValueError:
        print('Invalid Input!')
    
    entry = input('Enter a number: ')

for i in numbers :
    sum += i
    count += 1

avg = sum / count

print(sum, count, avg)
