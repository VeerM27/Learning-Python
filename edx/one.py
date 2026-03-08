def greet(input):
    if "hello" in input:
        return "Hello there!"
    else:
        return "I'm not sure how to respond to that."

x = input("Please enter a greeting: ")

response = greet(x)
print(response)
