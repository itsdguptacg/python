# IPO Model
# Input : 
#     1 Number
# Processing:
#     Check if number modulo 2 is 0
# Output:
#     "Even" or "Odd"

# Algorithm
# 1. Start
# 2. Read number
# 3. If number % 2 == 0, print "Even"
# 4. Else, print "Odd"
# 5. Stop

# Dry Run 1
# Input : 10
# Condition : 10 % 2 == 0 (True)
# Output : Even

# Dry Run 2
# Input : 7
# Condition : 7 % 2 == 0 (False)
# Output : Odd

# Python Solution
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")