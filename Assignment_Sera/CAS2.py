##
3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85. 
##

## Solution

#1. Take the input from the user
grade = input("Enter Score: ")
score = float(grade)

#2. First condition for score value should be in range of 0.0 to 1.0
if score >= 0.0 and score <= 1.0:
#Now check for the score & print accordingly
    if score >= 0.9:
        print ('A')
    elif score >= 0.8:
        print ('B')
        
    elif score >= 0.7:
        print ('C')
    elif score >= 0.6:
        print ('D')
    elif score < 0.6:
        print ('F')
        
#2. Else Condition to give user hint to provide value in range.    
else:
    print("Please Provide score in Range of 0.0 to 1.0")
