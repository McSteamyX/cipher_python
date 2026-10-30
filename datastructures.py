#imagine you are building a school system that calculates the average marks

marks=[65,89,64,89,90]
total=0
for x in marks:
    total=total+x
average=total/len(marks)
print(f"Total marks: {total}")
print(f"Average is {average}")     

#create  a complex calculator using inputoutput and controlflows
print("Operators: +,-,/,*,&,//")
while True:
 
 operator=input("Enter any of these operators(+,-,*,/,%,//) or 'q' to quit: ").lower()

 if operator == "q":
    print("Calc Terminated")
    break

 if operator in ["+","-","*","/","%","//"]:
    try:
        x=float(input("Enter the first number: ")) 
        y=float(input("Enter the second number: "))

        if operator =="+":
            print(f"The sum of {x} and {y} is {x+y}") 
        elif operator == "-":
            print(f"The difference of {x} and {y} is {x-y}")
        elif operator == "*":
            print(f"The product of {x} and {y} is {x*y}")
        elif operator == "%":
            print(f"The modulus of {x} and {y} is {x%y}")
        elif operator == "//":
            print(f"The floor division of {x} and {y} is {x//y}")
        elif operator == "/":
            if y!=0:
                print(f"The quotient of {x} and {y} is {x/y}") 
            else:
                print("Mathematical error")
    except  ValueError:
        print("Invalid input! Enter numbers only")
 else:
   print("Invalid operator")     
