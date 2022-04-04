lst=[]
print("Enter 10 numbers:")
odd_sum=0
even_sum=0
for i in range(10):
    lst.append(int(input("Enter number:")))

for i in range(10):
    if lst[i]%2:
        odd_sum +=lst[i]
    else:
        even_sum +=lst[i]   

# second way to write code to add odd or even numbers of list
for item in lst:
    if item%2:
        odd_sum +=item
    else:
        even_sum +=item

print(f"Even sum={even_sum}\nOdd sum={odd_sum}")