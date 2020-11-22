x=int(input("how many numbers? "))
sayac=0
for i in range(x):
 i=int(input("enter an value: "))
 if i%2==0:
   sayac+=1
print(sayac*100/x, "%")
