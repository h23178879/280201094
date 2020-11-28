
x=input("enter an email: ")
x=x.lower()
y=x.split("@")
z=y[0]
z1=y[1]
n=z.replace(".","")
if n=='ceng113' and z1=='example.com':
  print('correct')
else:
  print('wrong')