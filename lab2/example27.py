sum = 0
count = 0
x = input("Enter an integer (negative to quit) >> ")
x = int(x)
while x >= 0:
  sum = sum + x
  count = count + 1
  x = input("Enter an integer (negative to quit) >> ")
  x = int(x)
  print("The average is", sum / count)