# functions

def minimum(a,b,c):
    if a<b and a<c:
        print("a is minimun")
    elif b<a and b<c:
        print("b is minimum")
    elif c<a and c<b:
        print("c is minimum")
    elif a==b<c :
        print("a and b are minimum")
    elif b==c<a :
        print("b an c are minimum")
    elif a==c<b :
        print("a and c are minimum")
    elif a==b and b==c and c==a :
        print("They are equal")
    else:
        print("Invalid")     

a = int(input("Enter value of a ==>"))
b = int(input("Enter value of b ==>"))
c = int(input("Enter value of c ==>"))
minimum(a,b,c)



# --------------------------------------------------

# function arguments


print("ADDITION")

def add(a=3,b=5):
    add = a+b
    return add

a = int(input("Enter first number ==>"))
b = int(input("Enter second number ==>"))

result = add(a,b)
print("The addition is ==>",result)


# -----------------------------------------------------

print("AVERAGE")
def average(a,b,c,d):
    average = (a+b+c+d)/4
    return average

a = int(input("Enter first number ==>"))
b = int(input("Enter second number ==>"))
c = int(input("Enter third number ==>"))
d = int(input("Enter forth number ==>"))

ave = average(a,b,c,d)
print("The average is :" ,ave)    

# ------------------------------------------------------

print("difference")

def minus(a,b):
    minus = a-b
    return minus

a = int(input("Enter first number ==>"))
b = int(input("Enter second number ==>"))

diff = minus(a,b)
print("The difference is :",diff)

# ------------------------------------------------------------

print("MULTIPLICATION")

def multiply(a,b):
    multiply = a*b
    return multiply

a = int(input("Enter first number ==>"))
b = int(input("Enter second number ==>"))

result = multiply(a,b)
print("The multiplication is ==>",result)


# --------------------------------------------------------






















