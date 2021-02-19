str1 = input() #Ram is a good boy.
strlst = str1.split(" ")
strzero = ''
strone = ''
strtwo = ''
#inplace reverse
for i in strlst:
    strone = strone + i[::-1] + ' ' 
print(*strone)

#complete Reverse
for i in strlst[::-1]:
    strtwo = strtwo + i[::-1] + ''
print(*strtwo)

#simple Reverse
for i in strlst[::-1]:
    strzero = strzero + i 
print(*strzero)

