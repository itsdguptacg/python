marks=int(input("Enter the marks : "))
if marks>=90:
    print("Excellent")
elif marks>=75 and marks<=89:
    print("Good")
elif marks>=40 and marks<=74:
    print("Pass")
else:
    print("Fail")