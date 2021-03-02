#Program to check a String is palindrome or not?
#eg. RadaR, Dad

def palindrome(str1):
    l = 0 #lower Index
    h = len(str1) - 1 #upper Index
    str1 = str1.lower()
    while l < h :
        if str1[l] != str1[h]:
            return False
        else:
            l += 1
            h -= 1
    return True

#driver code
inputStr = input('Please input a string.\n')
print('Is String palindrome :', palindrome(inputStr))

