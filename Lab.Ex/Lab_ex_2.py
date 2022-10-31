import math

# EX.1 Check if a number is palindrome
"""
num = int(input("Enter a value: "))


def is_palindrome():
    global num
    temp = num
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    if num == reverse:
        return True
    else:
        return False


print(is_palindrome())
"""

# EX.2 Replace all numbers bigger than N with 0
"""
n = int(input("Enter a number: "))
arr = [num for num in range(20)]


def replace_with_zero():
    global arr
    global n

    for el in range(len(arr)):
        if arr[el] > n:
            arr[el] = 0

    print(arr)


replace_with_zero()
"""

# EX.3 Basic calculator
"""
x = int(input("Enter value for X: "))
y = int(input("Enter value for Y: "))
print("Options: add, sub, mul, div")
action = input("Enter action to perform: ")


def add():
    global x
    global y
    print(x + y)


def sub():
    global x
    global y
    print(x - y)


def mul():
    global x
    global y
    print(x * y)


def div():
    global x
    global y
    print(x / y)


if action == "add":
    add()
elif action == "sub":
    sub()
elif action == "mul":
    mul()
elif action == "div":
    div()
"""

# EX.4 Fill a list with squared elements in range from 1 to 30
"""
#First method
squares = [x**2 for x in range(1, 31)]
print(squares)
"""

"""
#Second method
list = []


def list_sq(list):
    for i in range(1, 30 + 1):
        i = i ** 2
        list.append(i)
    print(list)


list_sq(list)
"""
# EX.5 Calculate factorial of a number
n = int(input("Enter number: "))
print(math.factorial(n))


def fac(n):
    fact = 1

    for i in range(1, n+1):
        fact *= i

    print(f'Factorial of {n} is: ', fact)


fac(n)
