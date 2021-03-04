#Method to remove any given character from a String.

def remove_char(str1,i):
    lst = list(str1)
    lst.remove(i)
    print(''.join(lst))




String = input('Enter String \n')
Ch = input('Enter Character to remove from String.\n')
remove_char(String,Ch)


