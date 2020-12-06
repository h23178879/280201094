number = 1
while number < 10:
  print(number)
  if number == 6:
    break
  number+=1



number = 1
while number < 10:
  number+=1
  if number%2==0:
    continue
  print(number)


friends=['ahmet', 'mehmet', 'ebru', 'mahmut', 'ayse']
t=0
while t<len(friends):
  friend=friends[t]
  t=t+1
  if friend=='mahmut':
    continue
  print(friend)


  friends=['ahmet', 'mehmet', 'ebru', 'mahmut', 'ayse']
for x in friends:
  if x == 'mahmut':
    continue
  print(x)