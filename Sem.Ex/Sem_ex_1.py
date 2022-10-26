"""
# EX.1
a = int(input("A = "))
b = int(input("B = "))

c = a * b

print(a + b)
print(c)
"""


# EX.2
"""
def func(a):
    b = a
    c = a + b * 5
    return c


a = int(input("A = "))
sum = func(a)

print(sum)
"""


# EX.3
"""
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]

print(arr1+arr2)
"""


# EX.4
"""
name = input("Enter desired name: ")
searched_character = input("Enter a character to search for: ")

for el in name:
    if searched_character == el:
        print(True)
        break
    elif searched_character != el:
        continue
"""

# EX.5
# print(int(input()) * int(input()) * int(input()))

# EX.6
"""
a = int(input("A = "))
b = int(input("B = "))

print(f'a = {a}; b = {b}; area = {a * b}')
"""