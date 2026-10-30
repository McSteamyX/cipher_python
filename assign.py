#Create a program that checks whether a number is odd or even
num=float(input("Enter any number:"))
if num%2==0:
    print(f"This number is even")
else:
    print(f"This number is odd")
#Create a program that checks between 3 numbers and determines which one is the largest
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
c=float(input("Enter the third number:"))
if a>b and  a>c:
    print(f"The largest number is {a}")
elif b>a and b>c:
    print(f"The largest number is {b}")
else:
    print(f"The largest number is {c}")

#Create a program that checks between 3 numbers and determines which one is the smallest
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
num3=float(input("Enter the third number:"))
if num1<num2 and  num1<num3:
    print("The smallest number is", num1)
elif num2<num1 and num2<num3:
    print("The smallest number is", num2)
elif num3<num1 and num3<num2:
    print("The smallest number is", num3)
else:
    print("Some numbers are equal or there is a tie")

 #Create a program that performs addition, subtraction, multiplication and division of two numbers based on user input
x=float(input("Enter the first number: ")) 
y=float(input("Enter the second number: "))
operator=input("Enter any of these operators(+,-,*,/): ")
if operator =="+":
 print(f"The sum of {x} and {y} is {x+y}") 
elif operator == "-":
 print(f"The difference of {x} and {y} is {x-y}")
elif operator == "*":
 print(f"The product of {x} and {y} is {x*y}")
elif operator == "/":
 if y!=0:
    print(f"The quotient of {x} and {y} is {x/y}") 
 else:
    print("Mathematical error")
else:
  print("Invalid operator")     

#GRADE STUDENTS MARKS
#Use the following grading system to grade student: marks 70 and above =A, 60-69 =B, 50-59=C, 40-49 =D, below 40=Fail

mark=float(input("Enter the marks scored by the student: "))
if mark<0 or mark>100:
    print("Invalid score")   
elif mark>=70:
   print("This student scored an A")
elif mark>=60:
   print("This student scored a B")
elif mark>=50:
   print("This student scored a C")
elif mark>=40:
   print("This student scored a D")
else:
   print("Failed")
           

#Create a program that lets a user input the marks of 3 subjects of a student and calculate the average

mark1=float(input("Enter the score of the subject 1: "))
mark2=float(input("Enter the score of the subject 2: "))
mark3=float(input("Enter the score of the subject 3: "))
average=(mark1+mark2+mark3)/3
print(f"The average score of {mark1}, {mark2} and {mark3} is {average}")  

#Write a program that calculates the electricity bill based on the number of units consumed, the billing rates are as follows:
#For the first 100 units: 25 per unit
#For the next 100 units(101-200): 35 per unit
#For the next 100 units(201-300): 45 per unit

unit=float(input("Enter the number of units consumed: "))
first_100=100*25
next_100=100*35
rem_unit=unit-100
rem1_unit=unit-200

if unit>300 or unit<0:
    print("Error")
elif unit<=100:
   print(f"Electricity bill is {unit*25}: ")
elif unit<=200:
   bill=first_100+(rem_unit*35)
   print(f"Electricity bill is {bill}: ") 
else:
   bill_1=first_100+next_100+(rem1_unit*45)
   print(f"Electricity bill is {bill_1}: ")     


