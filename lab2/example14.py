x = int(input("enter a year: "))
if x %400==0:
  print(x , "is a leap year.")
elif x%100==0:
  print(x , "is not a leap year.")
elif x%4==0:
  print(x , "is a leap year.")
else:
  print(x , "is not a leap year.")
  