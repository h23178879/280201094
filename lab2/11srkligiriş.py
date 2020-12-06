x=0
while (x != 'q'):
  x=int(input('sayı gir'))
  if x==0:
    print('sayı nötr:')
  elif x<1:
    print('sayı negatif')
  else:
    print('sayı pozitif')