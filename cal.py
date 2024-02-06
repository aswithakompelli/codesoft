def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
print("welcome to the calculator program")
choice=0
while True:
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    print("select an operation:")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    Choice=int(input("enter your choice(1-4):"))
    if choice==1:
        print("result:",add(num1,num2))
    elif Choice==2:
        print("result:",subtract(num1,num2))
    elif Choice==3:
        print("result:",multiply(num1,num2))
    elif Choice==4:
        print("result:",divide(num1,num2))
    else:
        print("invalid choice!")
        restart=input("do you want to calculate again?(yes/no)")
        if restart.lower()!="yes":
            break
        print("thank you for using the calculator program!")