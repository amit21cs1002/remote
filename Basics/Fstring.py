country="India"
name="Amit" 
print(f"Hello my name is {name} and I belong to {country}")  #fstring

a="Hello my name is {} and I belong to {}"
print(a.format(name,country)) #old format

print("Hello my name is" ,name, "and I belong to" ,country,) #normal

print("Hello my name is " +name, "and I belong to " + country) #concatination