A="abc def"
print(A[0])
print(len(A))
# N[0]="X" will not work
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
B=[5,[8,1],[15,10],[4]]
print(B[2][0])
print(len(B))
#L[0]=4 will work
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
C=["Zero","One","Two","Three"]
print(C[0])
print(C[1][1])
print(len(C))
print(len(C[1]))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
D="0123456789"
print(D[0:5:1])
print(D[0:5:2])
print(D[3:6:1])
print(D[7::])
print(D[::-1])
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

E=["one","two","three","four","five"]
E.append("new one")
print(E)
F=["one","two","three","four","five"]
F.remove("two")
print(F)
Q=["one","two","three","four","five"]
print(Q.index("four"))
W=["one","two","three","four","five"]
ekle=[1,2,3,4,5]
W.extend(ekle)
print(W)
R=["one","two","three","four","five"]
R.insert(1,"one")
print(R)
T=["one","two","three","four","five"]
silinen=T.pop(3)
print(T)
print(silinen)
Y=["one","two","three","four","five"]
Y.sort()
print(T)
U=["one","two","three","four","five"]
U.reverse()
print(U)
O=["one","two","two","three","four","five"]
n = O.count("two")
print(n)
print(O)