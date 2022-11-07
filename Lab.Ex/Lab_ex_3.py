import math
import random

# EX.1
'''
arr = random.sample(range(10, 1000), 11)
print(arr)
n = int(input("Enter number: "))
# idx = []
for el in range(len(arr)):
    if arr[el] > n:
        print(el)
# print(idx)
'''

# EX.2
'''
arr = ["sit", "Lorem", "amet", "ipsum", "dolor"]
print(arr)
# res = max(arr, key=len)
max_len = -1  # ?
for ele in arr:
    if len(ele) > max_len:
        max_len = len(ele)
        longest = []
        longest.append(ele)
    elif len(ele) == max_len:
        longest.append(ele)
print(longest)
'''

# EX.3
'''
arr = random.sample(range(10, 1000), 11)
print(arr)
# arr.sort()
# arr.sort(reverse=True)

if arr == sorted(arr):
    print("List is sorted in ascending order...")
elif arr == sorted(arr, reverse=True):
    print("List is sorted in descending order...")
else:
    print("List order is undefined...")
'''
