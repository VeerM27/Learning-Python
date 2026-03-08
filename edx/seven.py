name = input("What is your name?: ")

def sorter(name):
    match name:
        case "Veer":
            print("Veer shall be in Gryffindor")
        case "Prue":
            print("Prue shall be in Ravenclaw")
        case _:
            print("You shall be in Hufflepuff")

sorter(name)