a="Amit Singh!!!"
print(a[0:4])
print(len(a)) 
nm="Harry"
print(nm[-4:-2]) #5-4=1 5-2=-3 
#[1:3]
print(a.upper()) #to upper class
print(a.lower()) #to lower class
print(a.rstrip("!")) #to strip something from string
print(a.replace("Amit","Kunsh"))

b="11/12/22"
print(b.split("/"))

c="tHiS IS nOT HOw iT must BE" #fixes all the capitalisation errors
print(c.capitalize())
print(a.center(50)) #Moves to centre with spaces
print(len(a.center(50)))
print(len(a))
print(c.count("i")) #count occurrence of that world of letter


print(a.endswith("!")) #check if a word ends with a particular value
print(c.endswith("E"))
print(a.endswith("t",0,4))

print(c.find("mustk")) #find index of first occurance
print(c.index("must")) #raise error if unable to find 
print(a.isalnum()) #check if string is Alphanumeric only
print(nm.isalnum())

print(a.islower()) #check if all are smol letter
d="hey \n"
print(d)
print(d.isprintable()) #can be printed ?
e=" "
print(c.isspace()) #check for space
print(e.isspace())

f="Hello My Name Is Amit"
print(f.istitle()) # check if each Letter is capital or not