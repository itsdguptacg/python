# Problem 4: Classify a number as positive, negative, or zero.
#
# What is being asked? Determine the number's sign.
# Input: One number.
# Output: positive, negative, or zero.
# Conditions: number > 0 -> positive; number < 0 -> negative; otherwise -> zero.
# Constraints: None are stated.
# Steps:
# 1. Read the number.
# 2. Compare it with zero.
# 3. Print the matching classification.

number = float(input())

if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")
