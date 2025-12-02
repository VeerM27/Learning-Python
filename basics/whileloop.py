def payroll(x, y):
    while True:
        try:
            x = int(x)
            break
        except:
            print('Please enter a valid value!')
            x = input('Enter hours: ')

    while True:
        try:
            y = float(y)
            break
        except:
            print('Please enter a valid value!')
            y = input('Enter rate: ')

    return x * y

hours = input('Enter hours: ')
rate = input('Enter rate: ')

pay = payroll(hours, rate)

print('Your total pay is ', pay)
