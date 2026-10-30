#loops
for i in range(1,11):
    print("Good morning sleepy head")

friends=["Ella","Abby","Kyler","Kibet","Debo"]

for f in friends:
    print(f"Happy Belated Birthday! {f}")

#calculate the expense that you brought
# bread ksh 90
# milk ksh 120
# sugar ksh 160

my_shopping=[90,120,160]
total=0
for m in my_shopping:
    total=total+m
print(f"Total is {total}")  

#Imagine you have 5 customers and each pay you 100. Create a script to get the total
total=0
for j in range(1,6):
 total=total+100
print(f"Total money collected is: {total}") 


#while loop
x=0
while x<=10:
   print(x)
   x+=2

#Imagine you want to save starting with 0 balance and save 100 daily until you have 1000

s=0
while s<1000:  
   print(f"Money saved: {s}")
   s+=100  
print("Congratulations you have reached your target")

