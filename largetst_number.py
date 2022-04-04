lst=[]
print("Enter 10 numbers:")
for i in range(10):
    lst.append(int(input("Enter number:")))

largest_No=lst[0]
for i in range(len(lst)-1):
    if largest_No<lst[i+1]:
        largest_No=lst[i+1]

print("Largest number=",largest_No)        