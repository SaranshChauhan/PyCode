ip = input()
while( ip == 'y' ):
    n = int(input())
    flag = False
    for i in range(2,n-1):
        if( n % i == 0):
            flag = True
            break
        else:
            flag = False

    if (flag == False):
        print("{} is a Prime Number.".format(n))
    else:
        print("{} is not a Prime Number.".format(n))

       