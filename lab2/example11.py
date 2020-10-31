m=float(input("please enter first a month after a day such as'mm.dd' : "))
if 03.20<m<=06.21:
  print("SPRING!!!")
elif 06.21<m<=09.22:
  print("SUMMER!!!")
elif 09.22<m<=12.21:
  print("AUTUMN!!!")
elif 12.21>m>12.30 or 01.01<m<03.20:
  print("WINTER!!!")
else:
  print("this date is wrong!")
