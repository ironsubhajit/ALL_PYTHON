'''
day 8
'''
'''
num = int(input("test no:"))

phone_book = {}

for i in range(0, num):
    entry = str(input("name & no.:")).split(" ")

    name = entry[0]
    phone = entry[1]
    phone_book[name] = phone

for j in range(0, num):
    name = str(input("name to check:"))

    if name in phone_book:
        phone = phone_book[name]
        print(name + "=" + phone)
    else:
        print("Not found")
'''
##the right one: 
n = int(input())
name_numbers = [input().split() for _ in range(n)]
phone_book = {k: v for k,v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print('%s=%s' % (name, phone_book[name]))
        else:
            print('Not found')
    except:
        break
