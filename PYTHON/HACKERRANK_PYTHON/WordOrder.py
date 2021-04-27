'''
using this for time complexity and insert order sequence
ordedDict remembers its insert order key, value
'''
from collections import OrderedDict as OD

n = int(input())
order_dict = OD()

for i in range(n):
    word = input()
    if word not in order_dict:
        order_dict[word] = word
    else:
        order_dict[word] = order_dict[word] + ' ' + word

unique_word = len(order_dict.keys())
occurence = " ".join(str(len(value.split(" "))) for key,value in order_dict.items())
print(unique_word)
print(occurence)


