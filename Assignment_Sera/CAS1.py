##
3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use input to read a string and float() to convert the string to a number. 
Do not worry about error checking the user input - assume the user types numbers properly. 
##

##Solution

#1. Take the input from User

hrs = input("Enter Hours:") 
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

#2. Put condition, if hours are equal to 40, multiple "hours" with "rate" & Return
if ( h <= 40 ):
   print(h * r)

#3. Put Another Comdition, If hours are greater than 40, multiple "Extra hours" with "rate" & 1.5 times, add the value to the gross pay ie. (rate*hours) and Return
elif ( h > 40 ):
    print((r*40) +( h - 40 ) * r * 1.5)
