# Calculate the surface of a circle with a diameter of 10 (radius^ * pi)
import math


# define the diameter
diameter = input("Insert the diameter:\n")

# convert to float
diameter_float = float(diameter)

# radius
radius = diameter_float / 2

# calculate
size = math.pow(radius, 2) * math.pi

# round the size
size_rounded = round(size, 2)

# print the result
print(f"The size is: {size_rounded}")

pass