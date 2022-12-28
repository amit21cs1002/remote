import time
a=int(input("Enter the first number: "))
b= int(input("Enter the second number: "))
c=input("choose the operation: ")
time=time.strftime("%H:%M:%S")

match c:

 case "+":

    print("Current time is :" ,time)   
    print(a+b)

 case "-":
                    if a>b:
                                        print(a-b)
                    else:
                                        print(b-a)

   # print(a-b)   

 case"*":
    print(a*b)

 case"/":
    print(a/b)

 case"%":
    print(a%b)

 case"e":
    print(a**b)   

 case default:
    print("Unexpected operation")                   



   