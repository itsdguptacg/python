# Problem 5: Apply a 10% discount when the price is at least 1000.
#
# What is being asked? Calculate the final price after any applicable discount.
# Input: The item's price.
# Output: The final price.
# Conditions: Price >= 1000 -> discount is 10%; otherwise there is no discount.
# Constraints: None are stated.
# Steps:
# 1. Read the price.
# 2. If it is at least 1000, multiply it by 0.90.
# 3. Otherwise, keep the original price.
# 4. Print the final price.

price = float(input())

if price >= 1000:
    final_price = price * 0.90
else:
    final_price = price

print(final_price)
