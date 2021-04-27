from itertools import permutations


def main(per_list, n):
    print(per_list)
    i_range = len(per_list)
    j_range = int(n)
    for i in range(i_range):
        greater_than_zero = 1
        #print("greater_than_zero is: ", greater_than_zero)
        for j in range(j_range):
            #print("return list status: ", greater_than_zero == j_range)
            if greater_than_zero == j_range:
                return per_list[i]
            #print("j+1 < j_range status: ", j+1 < j_range)
            if j+1 < j_range:
                frst_elem = per_list[i][j]
                scnd_elem = per_list[i][j+1]
                #print(frst_elem)
                #print(scnd_elem)
                #print("status: ", frst_elem & scnd_elem > 0)
                if frst_elem & scnd_elem > 0:
                    greater_than_zero += 1
                    #print("greater_than_zero is: ", greater_than_zero)
                else:
                    #print("breaking inner loop...")
                    break
    return -1


test_case = input()
for t in range(int(test_case)):
    N = int(input())
    output = main(list(permutations(range(1, N+1))), N)
    print(output)
