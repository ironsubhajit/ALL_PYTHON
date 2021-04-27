A=[]
B=[]
C=[]
r=int(input("Enter rows of A and B:"))
c=int(input("Enter columns of A and B:"))
print("Enter elements in A:")
for i in range(r):
        a=[]
        for j in range(c):
                a.append(int(input()))
        A.append(a)
print("Enter elements in B:")
for i in range(r):
        b=[]
        for j in range(c):
                b.append(int(input()))
        B.append(b)

for i in range(r):
        l=[]
        for j in range(c):
                l.append(0)
        C.append(l)
for i in range(r):
        for j in range(c):
                for k in range(c):
                        C[i][j]+=A[i][k]*B[k][j]
print("Matrix A:",A)
print("Matrix B:",B)
print("Multiplication:",C)

