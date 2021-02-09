import re
#\s: [\f\n\r\t\v]
#\S: except [\f\n\r\t\v]
fname = "Srone Codes"
if re.search("\w{2,20}\s\w{2,20}",fname):
	print("It's a Valid Name.")
else:
	print("Not a Valid Name.")