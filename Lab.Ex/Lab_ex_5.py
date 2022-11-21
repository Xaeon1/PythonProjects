import datetime
import calendar
import math
# EX.1
'''
try:
    input_num = int(input("Enter a number: "))
    if input_num <= 0:
        raise ValueError
    else:
        print(input_num ** 2)
except ValueError:
    print("Invalid input...")
'''

# EX.2
'''
try:
    month = int(input("Enter a month: "))
    year = int(input("Enter a year: "))

    if datetime.date(year, month, 13).weekday() == 0:
        print("True")
    elif 0 > month > 12 or 0 > year:
        raise ValueError
    else:
        print("False")
except ValueError:
    print("Invalid input...")
'''

# EX.3
'''
try:
    txt = input("Your input: ")

    if not txt.isdigit():
        for el in range(len(txt)+1):
            if txt[el].islower():
                print(el)
            else:
                continue
    else:
        raise TypeError
except TypeError:
    print("Invalid input...")
'''

# EX.4
'''
try:
    value = float(input("Enter money value: "))
    print("Currency options: BGN, EUR, TRY, USD")
    currency = input("Enter currency: ")
    while True:
        if currency == "BGN":
            print("EUR: ", round((value * 0.51), 2))
            print("TRY: ", round((value * 9.76), 2))
            print("USD: ", round((value * 0.52), 2))
        elif currency == "EUR":
            print("BGN: ", round((value * 1.96), 2))
            print("TRY: ", round((value * 19.10), 2))
            print("USD: ", round((value * 1.03), 2))
        elif currency == "TRY":
            print("BGN: ", round((value * 0.10), 2))
            print("EUR: ", round((value * 0.052), 2))
            print("USD: ", round((value * 0.054), 2))
        elif currency == "USD":
            print("BGN: ", round((value * 1.91), 2))
            print("EUR: ", round((value * 0.98), 2))
            print("TRY: ", round((value * 18.62), 2))
        elif currency == "EXIT":
            break    
        elif value <= 0:
            raise ValueError
        elif value.is_integer():
            raise TypeError
except ValueError and TypeError:
    print("Invalid input...")
'''

# EX. 5
'''
try:
    binary_num = int(input("Enter binary number: "), 2)

    if 0 < binary_num:
        print(hex(binary_num))
    else:
        raise ValueError
except ValueError:
    print("Invalid input...")
'''

# EX.6
'''
try:
    value = int(input("Enter value: "))
    print("Choices: RAD or DEG")
    choice = input("Enter choice: ")

    if choice == "RAD":
        print("DEG: ", round((math.degrees(value)), 2))
    elif choice == "DEG":
        print("RAD: ", round((math.radians(value)), 2))
    elif value < 0:
        raise ValueError
    elif choice != "RAD" or "DEG":
        raise TypeError
except ValueError or TypeError:
    print("Invalid input...")
'''
