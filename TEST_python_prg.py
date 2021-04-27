n = 3
list1 = list(map(int, input("->").split(sep=' ', maxsplit=n)))
max_height = max(list1)
cut_portion = []
for H in range(max_height):
    for h in list1:
        cut = (h-H)
        if cut  == 0:
            cut_portion.append(h)
        else:
            cut_portion.append(cut)
        print(cut_portion)
        check_list(cut_portion)
        if check_list == True:
            count++
        else

print(cut_portion)
