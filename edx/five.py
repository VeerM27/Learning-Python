def main(x):
    if 90 <= x <= 100:
        print("Your grade is A")
    elif x >= 80:
        print("Your grade is B")
    elif x >= 70:
        print("Your grade is C")
    elif x >= 60:
        print("Your grade is D")
    else:
        print("Your grade is F")


x = int(input("Enter your x: "))
main(x)