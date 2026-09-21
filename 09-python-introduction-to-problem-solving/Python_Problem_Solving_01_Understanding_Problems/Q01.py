# Problem 1: Take two numbers and print the larger number.
#
# What is being asked? Compare two input numbers and display the larger one.
# Input: Two numbers.
# Output: The larger number, or an equality message if neither is larger.
# Conditions: Compare the first number with the second; handle equal values.
# Constraints: None are stated.
# Steps:
# 1. Read both numbers.
# 2. Compare them.
# 3. Print the larger number, or report that they are equal.

first = float(input())
second = float(input())

if first > second:
    print(first)
elif second > first:
    print(second)
else:
    print("Both numbers are equal")
