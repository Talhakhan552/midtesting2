#-----------QUESTION NO.1-------------
# IF statement
# car purchase
budget=int(input("Plz enter your budget: "))

car_price=int(input("Enter car price: "))

if(budget>=car_price):
    print("You can buy this car :)")
else:
    print("You are out of budget :(")


    
# ----------QUESTION NO.2----------
# IF statement
# age classifier

age=int(input("Enter your age: "))

if(age<=10):
    print("You are very young:")
elif(age<=18):
    print("You are a Teenager ;)")
elif(age<=35):
    print("You are Adult :)")    
elif(age<=50):
    print("You are Middle aged :")
else:
    print("You are old :(")
    
    
    
# ------------QUESTION NO.3--------------
# Grade calculator

marks = int(input("Enter your marks ==>"))
# Total marks are out off 1100
percentage = (marks/1100)*100

print("Your percentage is ==>",percentage)

if(percentage>=90):
    grade = 'A+'
elif(percentage>=85):
    grade = 'A'
elif(percentage>=80):
    grade = 'B+'
elif(percentage>=75):
    grade = 'B'
elif(percentage>=70):
    grade = 'C+'
elif(percentage>=65):
    grade = 'C'
elif(percentage>=60):
    grade = 'D'
else:
    grade = 'F'
    
print("Your Grade is ==> ",grade)
 


# -------------QUESTION NO.4--------------
# Simple arithematic operator

num_1 = float(input("Enter 1st Number ==> "))
num_2 = float(input("Enter 2nd Number ==> "))

op = input("Enter an Operator (+,-,*,/) ==> ")

if(op == '+'):
    result = num_1+num_2
elif(op == '-'):
    result = num_1-num_2
elif(op == '*'):
    result = num_1*num_2
elif(op == '/'):
    if(num_2 == 0):
        result = "It is indivisible"
    else:
        result = num_1/num_2
else:
    print("Invalid Operator")
    
print("Answer :",result)

    

    
    
   