def greet():
    print("This is my first function")
greet()    

#function with parameters
def student(name,age,course):
    print(f"Student name is {name}")
    print(f"Student age is {age}")
    print(f"Student course is {course}")
student("Shania",19, "Computer Science")
student("Ella",20, "Commerce")
student("Abby",20, "Data Science") 
student("Asami",20, "Nursing")   

#function with return keyword
def prod_number(a,b):
    return a*b
result=prod_number(7,68)
print(f"The product is {result}")

def add_number(a,b):
    return a+b
result=add_number(7,68)
print(f"The sum is {result}")

def sub_number(a,b):
    return a-b
result=sub_number(96,68)
print(f"The difference is {result}")