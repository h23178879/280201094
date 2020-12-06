books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
bir=[]
iki=[]
book_dict={}
for i in books:
 char1=list(i) 
 char2=set(i)
 bir.append(len(char1))
 iki.append(len(char2))
 zippet=list(zip(bir,iki))
 for j in zippet: 
  book_dict.update({i:j})
for key,value in book_dict.items():
  print(key, value)
