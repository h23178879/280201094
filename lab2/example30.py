print("for exit write '0'!!!")
name=''
people={}
while (name != '0'):
  name=input('what is your name? ')
  yas=int(input('how old are you? '))
  if yas > 18:
   people.update({name: yas})
   print(people)
   liste=list(people.keys())
print('older then 18: ')
for i in liste:
  print(i)
