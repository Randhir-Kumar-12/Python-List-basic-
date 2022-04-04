lst=[]
print("Enter 10 numbers:")
for i in range(10):
    lst.append(int(input()))
print("Unsorted list:",lst) 

for i in range(len(lst)):
    count=1
    for j in range(len(lst)-count):
        if lst[j]>lst[j+1]:
            temp=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=temp
    count +=1  

print("Sorted list:",lst)          
