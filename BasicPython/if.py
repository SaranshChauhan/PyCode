import random
import os
import time

os.system("clear")
answer = input("Do you want a Quotes? ")

#In Python String always Return True if they aren't empty.

var = ["You are Worthy",
        "You can do anything",
        "You are the most beautiful mind of all time",
        "You should thankful to God always",
        "You can control your mind",
        "You run your mind, your mind does't run You",
        "You deserve all the happiness around the world",
        "You make a good decision Today!",
        "Stay motivated, Stay Healthy"]
#pos_dec = ["Yes","yes","y","Y"]
#pos_dec = ["yes","y"] #we can do without list 
#converted inputs to lower case & compare afterwards
#in pos_dec:
while "y" in answer.lower(): 
	print(random.choice(var))
	time.sleep(1.4)
	#print("                                                  ")
	#print("                                                  ")
	print("\n \nWanna here more motivation Quotes?? Put y or n")
	answer = input()
else:
	time.sleep(1.2)
	print("Didn't get it, Signing Off \nin..")

print(".1");time.sleep(.1)
print("..2");time.sleep(.1)
print("...3");time.sleep(.1)
print("....4");time.sleep(.1)
print(".....5");time.sleep(.1)
print("Good Luck Stay Blessed, :)")	