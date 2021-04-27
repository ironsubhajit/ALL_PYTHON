#HackerRank Python challenges
#merge the tools

def merge_the_tools(string, k):
    s = string
    length = len(s)
    step = int(length/k)
    for i in range(step):
        t = ''
        for c in s[i * k : (i + 1) * k]: #need to check the work function
            if c in t:
                continue
            t += c
        print (t)
        # your code goes here

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
