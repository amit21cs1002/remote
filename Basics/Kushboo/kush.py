import time as t
a="Welcome to KBC"
print(a.center(130))
b="(Kon Banega Karodpati)"
print(b.center(130))
w=0
name=input("Enter your name :")
t.sleep(1)

c="Lets Begin"
print(c.center(130))

def hello():
 print("\n")                   
 print("Hello " +name)
 print("You have won Rs.",w)


#Question1
print("Q.1 Which is best programming language ?")
t.sleep(0.5)
print("a.Java                                   b.Python")
print("c.C                                      d.Rust")
ans=input("Enter the option: ")
t.sleep(1)

if ans=="b":
                    print("Congrats!! Your answer is correct")
                    t.sleep(0.5)
                    print("You won Rs.10K")
                    w=w+10000
                    print("Your current winning is ", w)
else:
                    print("Sorry!! Your answer is incorrect: ")
                    print("You won Rs.00")
                    print("Correct answer is Python")
                    print("Your current winning is " , w)
                    hello()
                    quit()
                    
print("\n")
#Question2
print("Q.2 Which is best chocolate ?")
t.sleep(0.5)
print("a.JavaPine                                   b.Cocothon")
print("c.Coco                                       d.JustRust")
ans=input("Enter the option: ")
t.sleep(1)

if ans=="c":
                    print("Congrats!! Your answer is correct")
                    t.sleep(0.5)
                    print("You won Rs.20K")
                    w=w+20000
                    print("Your current winning is " , w)
else:
                    print("Sorry!! Your answer is incorrect: ")    
                    print("Correct answer is Coco")  
                    print("Your current winning is " ,w)
                    hello()
                    quit()
print("\n")
#Question3
print("Q.3 Which is your fav. member from Blackpink ?")
t.sleep(0.5)
print("a.Rose                                      b.jenny")
print("c.lisa                                      d.Jisoo")
ans=input("Enter the option: ")
t.sleep(1)

if ans=="a":
                    print("Congrats!! Your answer is correct")
                    t.sleep(0.5)
                    print("You won Rs.50K")
                    w=w+50000
                    print("Your current winning is " , w)
else:
                    print("Sorry!! Your answer is incorrect: ")   
                    print("Correct answer is Rose") 
                    print("Your current winning is " , w)
                    hello()
                    quit()
print("\n")
#Question4
print("Q.4 Which is the best dance partner ")
t.sleep(0.5)
print("a.Snake                                            b.Human")
print("c.A coffe cup                                      d.Your MOm")
ans=input("Enter the option: ")
t.sleep(1)

if ans=="d":
                    print("Congrats!! Your answer is correct")
                    t.sleep(0.5)
                    print("You won Rs.100K")
                    w=w+100000
                    print("Your current winning is " , w)
else:
                    print("Sorry!! Your answer is incorrect: ")   
                    print("Correct answer is Your Mom") 
                    print("Your current winning is " , w)
                    hello()
                    quit()
print("\n")
#Question5

print("Q.5 Which is your fav. game ?")
t.sleep(0.5)
print("a.BGMI                                     b.Phasmophobia")
print("c.GTA                                      d.Minecraft")
ans=input("Enter the option: ")
t.sleep(1)

if ans=="a":
                    print("Congrats!! Your answer is correct")
                    t.sleep(0.5)
                    print("You won Rs.200K")
                    w=w+200000
                    print("Your current winning is " , w)
else:
                    print("Sorry!! Your answer is incorrect: ")    
                    print("Correct answer is BGMI") 
                    print("Your current winning is " , w)
                    hello()
                    quit()
print("\n")