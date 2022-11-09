# EX.1
import math
import random
'''
r = float(input("Enter radius: "))

print("Area: ", round(math.pi*(r**2), 3))
print("Perimeter: ", round(2*math.pi*r, 3))
'''

# EX.3
'''
a = float(input("Enter value for A: "))
b = float(input("Enter value for B: "))
h = float(input("Enter value for H: "))

print("Area: ", round((a+b)*h/2, 2))
'''

# EX.3
'''
worked_hours = float(input("Enter worked hours: "))
pay_per_hour = float(input("Enter hourly wage: "))

print("Salary: ", worked_hours*pay_per_hour)
'''

# EX.4
'''
num = random.randint(0, 100)
print(num)

print("num > 50" if num > 50 else "num < 50")
print("Num is even" if num % 2 == 0 else "Num is odd")
'''

# EX.5
'''
age = random.randint(0, 15)
print("Age: ", age)
if age < 5:
    print("Free!")
elif 5 < age < 10:
    print("Half!")
else:
    print("Full!")
'''

for i in range(20, 0, -2):
    if i == 10:
        continue
    print(i)
