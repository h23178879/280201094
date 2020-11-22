psw="halil123"
x=input("enter the password: ")
while (x != psw):
  print("wrong")
  x=input()
  if (x=='help'):
    print (psw[0])
  elif(x == psw):
     print("welcome")

