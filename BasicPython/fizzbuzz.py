# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers that are multiples of both three and five print "FizzBuzz".

# Tip: % (modulo) tells you what's left over when you divide one number by another
# ex. number % 3 == 0

for i in range(1,100):
	if (i % 3 == 0 and i % 5 == 0):
		print("FizzBuzz")
	elif (i % 5 == 0):
		print("Buzz")
	elif (i % 3 == 0):
		print("Fizz")
	else:
		print