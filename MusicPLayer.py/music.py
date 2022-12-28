import pywhatkit
# a="baby"
# b="gypsey"
com=input("Enter a song: ")
if com=="baby" or com=="gypsey" :
 print("Sorry that song sucks")                   
else: 
 pywhatkit.playonyt(com)