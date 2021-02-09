import os

os.sytem("clear") #to Clear screen on Linux Os Terminal for Windows use "clr"
n = int(input().strip())

if n % 2 == 0:
    if n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    else:
        print("Not Weird")
else:
    print("Weird")
