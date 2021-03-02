#Program to check a String is palindrome or not?
#eg. RadaR, Dad

def palindrome1(str1):
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


def palindrome2(str1):
    str1 = str1.lower()
    lst1 = list(str1)
    lst2 = lst1[::-1]
    if lst1 == lst2:
        return True
    else:
        return False


#driver code
inputStr = input('Please input a string.\n')
print('Is String palindrome by method 1 :',palindrome1(inputStr)) #calling method one
print('Is String palindrome by method 2:',palindrome2(inputStr)) #calling method two

