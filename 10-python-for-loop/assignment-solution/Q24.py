a=input("Enter the String : ").lower()
count=0
for i in a:
    if i=="a":
        count+=1
print(f"Number of a in {a} is {count}")