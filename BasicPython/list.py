import time
import os

os.system("clear")

the_count = [1, 2, 3, 4, 6]
stocks = ["AAPL", "GOOG", "TSLA"]
random_things = ["Puppies", 55, "Anthony Weiner", 1/2, ["Oh no", "A list inside a list"]]
people = []
print("First List")
for i in the_count:
	print(i)
print("\nSecond List")
time.sleep(1.3)
for j in stocks:
	print(j)
print("\nThird List")
time.sleep(1.3)
for k in random_things:
	print(k)
#add items to list
people.append("Dani")
people.append("Mani")
people.append("Kani")
print("\n\nBefore Remove")
print(people)
#remove an item
print("\n\nAfter Remove")
people.remove("Mani")
print(people)

print("\nPrinting out the Square of a number")
#square of a number
for i in range(1,11):
	print(i*i)