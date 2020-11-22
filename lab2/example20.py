no1 = int(input("Enter the number :"))
no2= int(input("Enter the number :"))
count=0
minn=min(no1,no2)
for i in range(len(str(minn))):
  if str(no1)[-i]==str(no2)[-i]:
    count+=1
print(count)

