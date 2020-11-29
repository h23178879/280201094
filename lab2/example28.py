sum = 0
count = 0
x = input("Enter an integer (empty to quit) >> ")
while x != "":
  x = int(x)
  sum = sum + x
  count = count + 1
  x = input("Enter an integer (empty to quit) >> ")
  print("The average is", sum / count)