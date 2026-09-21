# IPO Model
# Input : 
#     3 Numbers
# Processing:
#     Compare numbers to find the largest
# Output:
#     The largest number

# Algorithm
# 1. Start
# 2. Read num1, num2, num3
# 3. If num1 >= num2 and num1 >= num3, max = num1
# 4. Else if num2 >= num1 and num2 >= num3, max = num2
# 5. Else max = num3
# 6. Print max
# 7. Stop

# Dry Run 1
# Inputs : 10, 25, 15
# Condition : 25 >= 10 and 25 >= 15 (True)
# Output : 25

# Dry Run 2
# Inputs : 5, 5, 5
# Condition : 5 >= 5 and 5 >= 5 (True)
# Output : 5

# Python Solution
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 >= n2 and n1 >= n3:
    print(n1)
elif n2 >= n1 and n2 >= n3:
    print(n2)
else:
    print(n3)