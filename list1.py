
expense=[2200,2350,2600,2130,2190]
print("Expenses form Jan to May:", expense)
extr_money=expense[1]-expense[0]
print("In Feb, We spent $",extr_money,"extra from to Janaury")

first_qter_exp=0
for i in range(0,3):
    first_qter_exp+=expense[i]
print("First quarter expense is $",first_qter_exp)

key=2000
print("we spent exacctly $2000 dollors in any month")
print(key in expense)

jun_exp=1980
expense.append(1980)
print("Expenses form  Jan to Jun:", expense)

expense[3]=1930
print("We got a refund of $200 in April")
print(expense)



