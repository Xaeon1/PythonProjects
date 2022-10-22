from asyncio import selector_events
from cmath import sin
import math

angle_degrees = float(input("Input degrees of an angle:"))

# print(angle_degrees)

degrees_to_radians = float((angle_degrees*math.pi)/180)

print(math.sin(degrees_to_radians))

# print(degrees_to_radians)