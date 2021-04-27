A=int(input("enter "))
for i in range(len(A)): 
  
    # iterating by coloum by B  
    for j in range(len(B[0])): 
  
        # iterating by rows of B 
        for k in range(len(B)): 
            result[i][j] += A[i][k] * B[k][j] 
  
for r in result: 
    print(r) 
