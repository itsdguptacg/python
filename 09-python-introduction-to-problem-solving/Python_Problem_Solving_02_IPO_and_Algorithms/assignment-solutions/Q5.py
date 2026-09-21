# IPO Model
# Input : 
#     Price (1 Number)
# Processing:
#     Apply 20% discount if price >= 2000
# Output:
#     Final price

# Algorithm
# 1. Start
# 2. Read price
# 3. If price >= 2000, calculate discount (price * 0.20) and subtract from price
# 4. Print final price
# 5. Stop

# Dry Run 1
# Input : 2500
# Condition : 2500 >= 2000 (True) -> 2500 - (2500 * 0.20)
# Output : 2000.0

# Dry Run 2
# Input : 1500
# Condition : 1500 >= 2000 (False)
# Output : 1500.0

# Python Solution
price = float(input("Enter price: "))
if price >= 2000:
    price = price - (price * 0.20)
print(price)
