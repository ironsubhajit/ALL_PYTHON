import re

s = input("s: ")
k = input("k: ")

pat = re.compile(k)
m = pat.search(s)
if not m: print("(-1, -1)")
while m:
    print(f"({m.start()}, {(m.end()-1)})")
    m = pat.search(s, (m.start()+1))
