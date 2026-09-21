# IPO Model
# Input : 
#     3 Marks
# Processing:
#     Calculate average. Check if average >= 40
# Output:
#     "Pass" or "Fail"

# Algorithm
# 1. Start
# 2. Read mark1, mark2, mark3
# 3. total = mark1 + mark2 + mark3
# 4. average = total / 3
# 5. If average >= 40, print "Pass"
# 6. Else, print "Fail"
# 7. Stop

# Dry Run 1
# Inputs : 50, 60, 40
# Condition : Avg = 150 / 3 = 50. 50 >= 40 (True)
# Output : Pass

# Dry Run 2
# Inputs : 30, 20, 35
# Condition : Avg = 85 / 3 = 28.33. 28.33 >= 40 (False)
# Output : Fail

# Python Solution
m1 = float(input("Enter mark 1: "))
m2 = float(input("Enter mark 2: "))
m3 = float(input("Enter mark 3: "))

avg = (m1 + m2 + m3) / 3

if avg >= 40:
    print("Pass")
else:
    print("Fail")