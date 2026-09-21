# IPO Model
# Input : 
#     Age (1 Number)
# Processing:
#     Check if age >= 18
# Output:
#     "Eligible" or "Not Eligible"

# Algorithm
# 1. Start
# 2. Read age
# 3. If age >= 18, print "Eligible to vote"
# 4. Else, print "Not eligible to vote"
# 5. Stop

# Dry Run 1
# Input : 20
# Condition : 20 >= 18 (True)
# Output : Eligible to vote

# Dry Run 2
# Input : 16
# Condition : 16 >= 18 (False)
# Output : Not eligible to vote

# Python Solution
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")