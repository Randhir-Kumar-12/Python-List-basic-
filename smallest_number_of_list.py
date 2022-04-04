lst=[]
print("Enter 10 numbers:")
for i in range(10):
    lst.append(int(input("Enter number:")))

smallest_No=lst[0]
for i in range(len(lst)-1):
    if smallest_No>lst[i+1]:
        smallest_No=lst[i+1]

print("Smallest number=",smallest_No) 