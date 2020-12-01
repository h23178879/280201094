first = input("Enter the first equation:""\n")
second = input("Enter the second equation:""\n")
x1 = 0
y1 = 0
c1 = 0
equal = 1
number = 1
isempty = 1
isX = 0
isY = 0
isnumber = 0
for i in first:
    
    if(i == '=' or i == '+' or i == '-'):
        if(isempty == 0):
            number *= equal
            if(isX == 1):
                x1 += number
            elif(isY == 1):
                y1 += number
            else:
                c1 += number
            number = 1
            isempty = 1
            isnumber = 0
            isX = 0
            isY = 0
    if(i == '='):
        equal = -1
        continue
    if(i == '+'):
        number = 1
        continue
    if(i == '-'):
        number = -1
        continue
    if(i >= "0" and i <= "9"):
        if(isnumber == 2):
            number*=10
            if(number < 0):
                number -= int(i)
            else:
                number += int(i)
            isnumber += 1
        elif(isnumber == 1):
            #print(number,i)
            number*=10
            if(number < 0):
                number -= int(i)
            else:
                number += int(i)
            isnumber += 1
        else:
            number *= int(i)
            isnumber += 1
        isempty = 0
    elif(i == "x"):
        if(isempty == 1):
            isempty = 0
        isX = 1
    elif(i == "y"):
        if(isempty == 1):
            isempty = 0
        isY = 1
number *= equal
if(isX == 1):
    x1 += number
elif(isY == 1):
    y1 += number
else:
    c1 += number
##2. equal
x2 = 0
y2 = 0
c2 = 0
equal = 1
number = 1
isempty = 1
isX = 0
isY = 0
isnumber = 0
for i in second:
    if(i == '=' or i == '+' or i == '-'):
        if(isempty == 0):
            number *= equal
            if(isX == 1):
                x2 += number
            elif(isY == 1):
                y2 += number
            else:
                c2 += number
            number = 1
            isempty = 1
            isnumber = 0
            isX = 0
            isY = 0
    if(i == '='):
        equal = -1
        continue
    if(i == '+'):
        number = 1
        continue
    if(i == '-'):
        number = -1
        continue
    if(i >= "0" and i <= "9"):
        if(isnumber == 2):
            number*=10
            if(number < 0):
                number -= int(i)
            else:
                number += int(i)
            isnumber += 1
        elif(isnumber == 1):
            #print(number,i)
            number*=10
            if(number < 0):
                number -= int(i)
            else:
                number += int(i)
            isnumber += 1
        else:
            number *= int(i)
            isnumber += 1
        isempty = 0
    elif(i == "x"):
        if(isempty == 1):
            isempty = 0
        isX = 1
    elif(i == "y"):
        if(isempty == 1):
            isempty = 0
        isY = 1
number *= equal
if(isX == 1):
    x2 += number
elif(isY == 1):
    y2 += number
else:
    c2 += number
print("Equations in the simplified form:")
str1 = ""
str1 += str(x1)
str1 += "x"
if(y1 >= 0):
    str1 += "+"
str1 += str(y1)
str1 += "y"
str1 += "="
str1 += str(c1*-1)
str2 = ""
str2 += str(x2)
str2 += "x"
if(y2 >= 0):
    str2 += "+"
str2 += str(y2)
str2 += "y"
str2 += "="
str2 += str(c2*-1)
print(str1)
print(str2)
print("Solution:")
#print(x1,y1,c1)
#print(x2,y2,c2)
x = 0
y = 0
if(y2 == 0):
    X = -c2/x2
    if(x1 == 0):
        y = -c1/y1
    else:
        y = (-c1 -x1*x)/y1
else:
    c = -c1 -(-c2/y2)*y1
    x = x1 + (-x2/y2)*y1
    x = c/x
str1 ="x="
if(x%1 == 0):
    x = int(x)
str1 += str(x)
print(str1)
if(y2 != 0):
    y = (-c2 -x2*x)/y2 
str1 ="y="
if(y%1 == 0):
    y = int(y)
str1 += str(y)
print(str1)