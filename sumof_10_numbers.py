lst=[]
print("Enter 10 numbers:")
sum=0
for i in range(10):
    lst.append(int(input("Enter number:")))
    sum= sum+ lst[i]

print(f"Sum of 10 number={sum}")