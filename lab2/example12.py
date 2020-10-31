a=int(input("enter value a of the quadratic equation: "))
b=int(input("enter value b of the quadratic equation: "))
c=int(input("enter value c of the quadratic equation: "))
delta=b**2-4*a*c
if delta>0:
  print("there are two real roots")
elif delta<0:
  print("there are two complex roots")
else:
  print("there is one real root")
  