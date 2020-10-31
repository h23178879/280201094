x=float(input("Enter your GPA: "))
y=float(input("Enter number of lectures: "))
if x<2.0 and y<47:
  print("Not enough number of lecture and GPA!")
elif x<2.0 and y>=47:
  print("Not enough GPA!")
elif x>=2.0 and y<47:
  print("Not enough number of lecture")
else:
  print("GRADUATED!!!")
  