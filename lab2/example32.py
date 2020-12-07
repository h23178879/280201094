employees={}
for i in range(5):
 x=(input("what is your name? "))
 y=int(input("what is your salary"))
 employees.update({x:y})
 listem=list(employees.items())
listem.sort()
listem.pop(0)
listem.pop(0)
print(listem)
for i in listem:
  print(i)
