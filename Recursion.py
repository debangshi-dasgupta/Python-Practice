# we use recursion at the time of creating factorial

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
input = int(input("Enter a number here:"))
print("The factorial is:",fact(input))


def hello():
    print("Hello World")
    return hello()
print(hello())