a=input("Enter the String : ")
count=0
for i in a:
    if "A"<=i<="Z":
        count+=1
print(f"Number of Upper Case Letters in {a} is {count}")