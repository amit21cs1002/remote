n=int(input("enter the value for factorial: "))
a=int(input("enter the value for fibo: "))
b=int(input("enter the value for nautural number :"))


def factorial(n):
                    if n==0:
                     return 1                   
                                       #factorial
                    else:
                     return  n*factorial(n-1)                    
        
c=factorial(6)
print(c)                         

#fibonaaci
def fib(a):
          if a==0:
                    return 0
#0 1 1 2 3 5 8 13 21 34 55 89 104
          elif a==1 or a==2:
                    return 1          
          else:
                    return fib(a-1)+ fib(a-2)                    
d=fib(11)
print(d)

# print natural number:
def natural(b):
  if b>1:
             natural(b-1)                 
  print(b)

natural(b)            

