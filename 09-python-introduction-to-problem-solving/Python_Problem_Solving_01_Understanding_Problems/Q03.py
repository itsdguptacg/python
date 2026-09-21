# Problem 3: Calculate a rectangle's area and perimeter.
#
# What is being asked? Find both measurements from the rectangle's dimensions.
# Input: The length and width.
# Output: The area and perimeter.
# Conditions: None are stated.
# Constraints: None are stated; dimensions are treated as numeric values.
# Steps:
# 1. Read the length and width.
# 2. Calculate area = length * width.
# 3. Calculate perimeter = 2 * (length + width).
# 4. Print both results.

length = float(input())
width = float(input())

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)
