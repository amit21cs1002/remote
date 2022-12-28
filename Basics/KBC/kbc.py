import time as t
name=input("Please enter your name to begin : ")
a="Welcome to KBC"
b="(Kon Banega Karorpati)"
c="Lets begin :)"
w=0
print(a.center(110))
print(b.center(110))
t.sleep(1)
print("\n")
print(c.center(110))
t.sleep(1)

#Question1
print("Q1. Which is best language for programming ?")
print("a.Swift                                      b.Ruby")
print("c.Python                                     d.Java")
a=input("\n Select the option: ")
t.sleep(1.2)
if a=="c":
  print("Congrats!!! your answer is correct. \n You have won Rs.10K")
  w=w+10000
else:
  print("Sorry!!! your answer is incorrect. \n Your have won Rs.00") 
  print("Python is correct answer")           
t.sleep(1)          

print(" Next Question :")
print("\n")
t.sleep(1)

#Question2
print("Q2. Which of these language is fastest :")
print("a.Java                                      b.Python")
print("c.C                                         d.Sql"   )
a=input("\n Select the option: ")
t.sleep(1.2)
if a=="c":
 print("Your answer is correct. \n You have won Rs. 20K")
 w=w+20000
else:
 print("Sorry!!! your answer is incorrect. \n Your have won Rs.00")
 print("'C' is correct answer")
print("\n") 
t.sleep(1)

print("\n Next Question :")
t.sleep(1)

#Question3
print("Q3. Which of these chocolate tastes best :")
print("a.JavaPine                                     b.Chocothon")
print("c.CocoC                                        d.Dairymilk"   )
a=input("\n Select the option: ")
t.sleep(1.2)
if a=="b":
 print("Your answer is correct. \n You have won Rs. 50K")
 w=w+50000
else:
 print("Sorry!!! your answer is incorrect. \n Your have won Rs.00")
 print("'CocoC' is correct answer")
print("\n")  
t.sleep(1)


print("\n Next Question :")
t.sleep(1)

#Question4
print("Q4. Which of these are best place to live :")
print("a.Javaland                                      b.Paris")
print("c.CCity                                         d.SnakeForest"   )
a=input("\n Select the option: ")
t.sleep(1.2)
if a=="d":
 print("Your answer is correct. \n You have won Rs. 100K")
 w=w+100000
else:
 print("Sorry!!! your answer is incorrect. \n Your have won Rs.00")
 print("'SnakeForest' is correct answer")
print("\n")  
t.sleep(1)

print("\n Next Question :")
t.sleep(1)

#Question5
print("Q5. Which of these is best dance partner :")
print("a.AcoffeeCup                                     b.Snake")
print("c.Diamond                                        d.Human"   )
a=input("\n Select the option: ")
t.sleep(1.2)
if a=="a":
 print("Your answer is correct. \n You have won Rs. 200K")
 w=w+200000
else:
 print("Sorry!!! your answer is incorrect. \n Your have won Rs.00")
 print("'AcoffeeCup' is correct answer")
print("\n")  
t.sleep(1)

print("Dear",name,)
print("The total amount you have won is : Rs." ,w,)

