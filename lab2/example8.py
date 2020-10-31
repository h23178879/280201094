x=int(input("first number: "))
y=int(input("second number: "))
z=int(input("third number "))
if x>y>z:
  print ("Max. value: " , x)
elif y>x>z:
  print("Max. value: ", y)
elif z>y>x:
  print("Max. value: ", z)
else:
  print("the numbers are equal")
