# Problem 2: Print a student's grade based on marks.
#
# What is being asked? Map the student's marks to the specified grade.
# Input: The student's marks.
# Output: A, B, C, or Fail.
# Conditions: 90 or above -> A; 75–89 -> B; 50–74 -> C; below 50 -> Fail.
# Constraints: None are explicitly stated.
# Steps:
# 1. Read the marks.
# 2. Check the grade ranges from highest to lowest.
# 3. Print the matching grade.

marks = float(input())

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")
