file_path = "my_data.txt"
my_file = open(file_path)
print ("File is opened!")
lines = my_file.readlines()
for line in lines:
      nums = line.split(' ')
      length = len(nums)
      print("Number of integers:",length)
      for num in nums:
       num = int(num)
       if num%2 == 0:
        out = num**2
       else:
        out = num//2
        print(out)
my_file.close()
print("End of file")
my_file = open(file_path)
print("File is re-opened!")
line = my_file.readline()
cnt = 1
while line != "":
      nums = line.split(' ')
      print("Reading line", cnt)
      cnt = cnt + 1
      if nums == ['3', '4\n']:
       print("Numbers 3 and 4 are found!")
       break
line = my_file.readline()
my_file.close()
print("Finished!")