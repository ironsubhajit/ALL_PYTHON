import math

'''
def main(total_que, ans_limit):
    resultant = total_que / ans_limit
    if resultant < ans_limit:
        ans = math.floor(resultant + 1)
        print(ans) 
    elif resultant >= ans_limit:
        ans = math.floor(resultant + 1)
        print(ans)
'''


def main(max_day_need, K, query_input):
    day = 1
    remain_ques = 0
    for i in range(max_day_need):
        day = (1 + i)
        query =
        if query < 5:
            print(day)
            return 0
        remain_ques = query - K
    day += 1
    print(day)
    return 0



test_case = input("t->")
for t in range(int(test_case)):
    input_list = list(map(int, input("i->").split()))
    N = input_list[0]
    K = input_list[1]

    query_input = list(map(int, input("q->").split()))

    total_que = sum(query_input)
    max_day_need = math.floor((total_que / K) + 1)
    '''
    if max_day_need < K:
        ans = math.floor(max_day_need + 1)
    elif max_day_need >= K:
        ans = math.floor(max_day_need + 1)'''

    main(max_day_need, K, query_input)
