# EX.1

arr = []
user_input = input("Enter number: ")

for el in range(len(user_input+1)):
    arr.append(el)

tup1 = tuple(arr)
print(tup1)
arr.sort(reverse=True)
tup2 = tuple(arr)
print(tup2)