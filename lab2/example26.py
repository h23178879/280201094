x=int(input("MxM enter a matris value: "))
for i in range(0,x):
  for j in range(0,x):
    if i==j:
      print('1',sep=" ", end=" ")
    else:
      print('0',sep=" ", end=" ")
  print()