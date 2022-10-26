"""
print("Hello World!")
print("o----")
print(" |||| ")
print("*" * 10)
"""

"""
price = 10  #int
rating = 4.9    #float
name = "Alex"   #String
is_published = True #Boolean
print(price)
"""

# Ex.1 We check in a patient named John Smith.
#      He's 20 years old and is a new patient.

input_full_name = input("Input patient's name: ")
input_age = int(input("Input patient's age: "))
is_existing_patient = False

if input_full_name == "John Smith" and is_existing_patient is False:
    print("Check in successful...")
else:
    print("This patient is already checked in...")

#
