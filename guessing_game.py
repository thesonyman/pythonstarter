#Script by thesonyman 
#I saw how small this repo for python was so I thought I would add somthing.
#This script is a number guessing game made in python 2.7 


import random
#This imports the random lib from the python default libs

x = random.randrange(1,100)

#this is the number that is generated 

#See this for more info on random https://docs.python.org/3/library/random.html


z = 0
# You have to define z though

cheatmode = 0 #cheats 1 is on anyother number is off 

while z < 2: #this limits the trys
  z += 1 # increments the number so you only get 2 trys
 
  y = int(raw_input("Guess A number between 1 and 100 \n"))
  #Ok you dont normaly keep track of vars in python but if you have to you can
  #because you cant compair a string to a int you have to convert the string to a int
  #so this is a normal input thing but it has a int(  ) in it the 2 paricicys go around it
  #this is actully kinda simular to java 



  if y == x: #compares your number to the actuall number
  	print ("wow you got it")
	break #stops the loop because its solved
    	
  else:
    h = 100 - x # gives you a hint  on a caculater you can do 100 - x and get the number
    print ("The number you are guessing for is %s from 100" %h) #the %s is basicly a sub for the var h 
    if cheatmode == 1: #cheats
        print(x)
print("The number was %s" %x)
