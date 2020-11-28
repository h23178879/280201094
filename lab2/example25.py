x=int(input("how many numbers? "))
liste=[]
liste2=[]
sayac=0
for i in range(x):
 i=int(input("enter an value: "))
 liste.append(i)
 print(liste)
 if i not in liste2:
   liste2.append(i)
   liste2.sort()
   liste2.reverse()
print(liste2)