
'''def check_input(n):
    if int(n) != -1:
        return n
    return None


test = input()
for i in range(int(test)):
    x = list(map(check_input, input().split()))
    list_of_input = [int(n) for n in x if n != None]
    #print(list_of_input)
    count = 0
    list_for_sum = []
    even_no_index = []
    for j in list_of_input:
        if j % 2 == 0:
            index = list_of_input.index(j)+1
            even_no_index.append(index)
            elem = (j*index)
            list_for_sum.append(elem)
        if j > 30:
            count += 1

    avg = (sum(list_for_sum) / sum(even_no_index))
    print("{} {:.2f}".format(count, avg))
'''
'''import re
def check_num(stg):
    reg = r'^[0-9]{10}$'
    x = re.search(reg, stg)
    if x:
        return True
    else:
        return False


user = list(input("->").split(" "))
if len(user)<6 or len(user)>6:
    print("INPUT LIMIT 5")
    exit(0)

count=0
for i in user:
    status = check_num(i)
    if status:
        count += 1
print(count)'''






