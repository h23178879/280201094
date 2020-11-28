numlist=['20']
grade=[]
sn=input("student number? ")
x=int(input("first midterm exam grade: "))
y=int(input("second midterm exam grade: "))
z=int(input("final exam grade: "))
a= 0.3*x + 0.3*y + 0.4*z
t=[x,y,z]
print("your average grade:",a)
if sn in numlist:
  grade.extend(t)
  print(grade)
else:
  print("your student number is not in list!")