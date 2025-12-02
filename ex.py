numbers = []
sum = 0
count = 0

while True :
    entry = input('Enter a number: ')
    if entry == 'done' :
        break
    try :
        num = int(entry)
    except ValueError :
        print('Invalid Input!')
        continue

    sum += num
    count += 1
    numbers.append(num)
   
avg = sum / count

print(sum, count, avg)
print(numbers)
