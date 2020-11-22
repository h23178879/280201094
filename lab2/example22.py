adet = int(input("How many fibonacci numbers: "))
sayac = 0
a = 1
b = 0
liste = []
while (adet > sayac):
    a = a + b
    a, b = b, a
    print(a)
    print(b)
    liste.append(b)
    sayac += 1
    print(liste)