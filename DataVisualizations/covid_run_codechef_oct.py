def main(N, K, X, Y):
    infect_city_list = []
    loop = True
    while loop:
        if X not in infect_city_list:
            infect_city_list.append(X)
            X = (X+K)%N
        else:
            loop = False
    if Y in infect_city_list:
        print("YES")
    else:
        print("NO")


test_case = input()
for t in range(int(test_case)):
    input_list = list(map(int, input().split(" ")))
    N = input_list[0]
    K = input_list[1]
    X = input_list[2]
    Y = input_list[3]
    main(N, K, X, Y)
