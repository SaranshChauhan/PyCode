import re
#\w: [a-z A-Z 0-9]
#\W: Other then [a-z A-Z 0-9]
ph = "123-344-6543"

if re.search("\w{3}-\w{3}-\w{4}",ph): #re.search("\d{3}-\d{3}-\d{4}",ph): work same
	print("Yes, It is Phone Number.")
else:
	print("Not a Valid Number.")

	