fileName = input("What file are the integers in? ")
infile = open(fileName,'r')
sum = 0
count = 0
for line in infile.readlines():
  sum = sum + int(line[:-1])
  count = count + 1
  print ("The average is", sum / count)