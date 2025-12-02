
def payroll(x, y):
    try:
        x = int(x)
    except:
        print('Please enter a valid value next time!')
        quit()

    try:
        y = float(y)
    except:
        print('Please enter a valid value next time!')
        quit()

    return x * y

hours = input('Enter hours: ')
rate = input('Enter rate: ')

pay = payroll(hours, rate)

print('Your total pay is ', pay)
