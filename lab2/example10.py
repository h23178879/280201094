x=int(input("How old are you? "))
if x<6 or x>60:
  print("Your ticket is free")
elif 6<=x<=18:
  print("You take 50% discount (1,5 TL)")
else:
  print("Your ticket is 3TL")
