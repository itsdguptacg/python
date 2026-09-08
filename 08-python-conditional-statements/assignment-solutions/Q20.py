number=int(input("Enter the number to check positive or negative: "))
if number!=0:
    if number>0:
        print(f"{number} is Positive")
    elif number<0:
        print(f"{number} is Negative")
    else:
        print("Invalid input")