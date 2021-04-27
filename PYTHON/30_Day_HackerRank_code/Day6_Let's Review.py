#@ironsubhajit
#HackerRank_Day06_Task:

# Enter your code here. Read input from STDIN. Print output to STDOUT
T=int(input())#input the no. of test cases
for i in range(0,T):
    string = input()#input the string   
    for j in range(0,len(string)):
        if j%2==0:
            print(string[j],end='')
    print(" ",end='')
    for j in range(0,len(string)):
        if j%2!=0:
            print(string[j],end='')
    print("")    
