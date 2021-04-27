'''number=[5,5,2,5,5,2,2,2]
for i in number:
    output=''
    for j in range(i):
        output+='*'
    print(output)
print("\n\n")

number1=[1]
for i in number1:
    output1=''
    for j in range(i):
        output=output+"*"
    print(output)
    '''
a=[10,2,3,10,4]
output=[]
for i in a:
    if i not in a:
        output.append(i)

print(a)
print(output)
print(len(a))