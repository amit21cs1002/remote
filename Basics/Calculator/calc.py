a=input("Enter the first number")
b=input("Enter the 2nd number")

#Add
ans=int(a)+int(b)
print("The addition of ",a,"and" ,b, "is" ,ans,)
ans=a+b
print("The concatination of " ,a, " and" ,b, "addition leds to",ans,)
#Sub
ans=int(a)-int(b)
print("The sub of",a, "and",b, "is" ,ans,)

#Product
ans=int(a)*int(b)
print("The product of",a, "and" ,b, "is", ans,)

#Modolus
ans=int(a)%int(b)
print("The remainder of",a, "and" ,b, "is", ans,)

#Divide
ans=int(a)/int(b)
print("The division of",a, "and" ,b, "is", ans, "With float points")

#Divide_With_Floats
ans=int(a)//int(b)
print("The division of",a, "and" ,b, "is", ans, "without float points")

#Exponential
ans=int(a)**int(b)
print("The exponential of",a, "and" ,b, "is", ans,)


print("Thank you")
for i in range (5):
    print("hello")
    if i==1 : print(1)
    if i==2 : print(2)
    if i==3: print(3)