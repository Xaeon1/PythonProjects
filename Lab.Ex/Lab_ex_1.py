# EX.1 Count syllables from user input
"""
user_input = input("Input text \n")

frequency = {}

for el in user_input:
    frequency[el] = user_input.count(el)

print(frequency)
"""

# Second solution
"""
def check_freq(x):
    return {c: x.count(c) for c in set(x)}
"""

# EX.2

user_input = int(input("Enter length of array: "))

array = []
dictionary = {}

for i in range(1, user_input+1):
    array.append(i)

array.sort(reverse=True)

for i in range(1,user_input+1):
    dictionary[i] = array[i-1]

print(dictionary)
"""
for el in array:
    dictionary.key = el
"""

