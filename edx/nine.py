def counter():
    while True:
        x = int(input("How many meows do you want? "))
        if x > 0:
            return x
        else:
            print("Please enter a positive integer.")

def meow(x):
    for _ in range(x):
        print("Meow")
        

x = counter()
meow(x)