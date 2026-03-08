def main(x, y):
    if x < y:
        print(f"{x} is less than {y}")
    elif x == y:
        print(f"{x} is equal to {y}")
    else:
        print(f"{x} is greater than {y}")


first = input("Enter the first number: ")
second = input("Enter the second number: ")
main(first, second)