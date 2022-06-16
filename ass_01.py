# task-01
given_str= 'HOusE'
up_case= 0
low_case= 0
for i in given_str:
    if ord(i)>=65 and ord(i)<=90:
        up_case+=1
    elif ord(i)>=97 and ord(i)<=122:
        low_case+=1
if up_case>low_case:
    print((given_str).upper())
else:
    print((given_str).lower())


# task-02
given_str= '213213'
num=0
str=0
for i in given_str:
    if ord(i)>=49 and ord(i)<=57:
        num+=1
    elif ord(i)>=65 and ord(i)<=90:
        str+=1
    elif ord(i)>=97 and ord(i)<=122:
        str+=1
if num== len(given_str):
    print('NUMBER')
elif str== len(given_str):
    print('WORD')
else:
    print('MIXED')


# task-03 not done
given_str= 'baNgladEsh'
str=''
str2=''
for i in given_str:
    if ord(i)>=65 and ord(i)<=90:
        str+= i
for m in given_str:
    if m == str[0]:
        print(m+1)
        if m== str[1]:
            break 
print(str)


# task-04
str1= 'harry'
str2= 'hermione'
common=0
for elem1 in str1:
    if elem1 in str2:
        common+=1
        print(elem1, end='')
for elem2 in str2:
    if elem2 in str1:
        common+=1
        print(elem2, end='')
if common==0:
    print('Nothing in common')


# task-05 not done
password= 'ohmybracu'
up=0
low=0
digit=0
for i in password:
    if ord(i)>=65 and ord(i)<=90:
        up+=1
    elif ord(i)>=97 and ord(i)<=122:
        low+=1
    elif ord(i)>=49 and ord(i)<=57:
        digit+=1
if up==0:
#  and low!=0 and digit!=0:
    print('Uppercase character missing.', end='')
elif low==0 :
# and up!=0 and digit!=0:
    print('Lowercase Missing.', end='')
elif digit==0 :
# and up!=0 and low!=0:
    print('Digit missing.', end='')
elif (up+low+digit)== len(password):
    print('Special character missing.', end='')
elif (up+low+digit)<len(password):
    print('OK')


# task-1--------list
given_number= input()
for elem in given_number:
    if elem.upper() == 'STOP':
        break
    else:
        print(given_number)


