#1.Write a function to find maximum of three numbers in python.

def max_num(val1,val2,val3):
    if val1 > val2 & val1 > val3:
        print(val1,"is the greatest")
    elif val2 > val1 & val2 > val3:
        print(val2,"is the greatest")
    else:
        print(val3,"is the greatest")

max_num(12,5,9)

#2. Write a python function to create and print a list where the values are square of numbers between 1 and 30.

def create_list():
    l = []
    for i in range(1,31):
        l.append(i**2)
    return l
print(create_list())

#3. Write a Python function that takes a number as a parameter and check if the number is prime or not.

def check_prime(num):
    if num == 1:
        print("It is not a prime number")
    if num == 2:
        print("It is a prime number")
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                print("It is not a prime number")
                break
            else:
                print("It is a prime number")
                break
num = int(input("Enter a number: "))
print(check_prime(num))



