d= {
    "brand":"Ford",
    "model":"Mastang",
    "Year": 1964
    }
print(d)
print("----------------------------------")
d["colour"]="red"#add key and value
print (d)
print("----------------------------------")
x=d.get("model")#find some iteam
print(x)
print("----------------------------------")
d["Year"]= 2018
print(d["Year"])
print("----------------------------------")
for x in d:#print by for loop
    print(x + "->" + str(d.get(x)))
print("----------------------------------")
for x,y in d.items():
    print(x,y)
print("----------------------------------")
if "model" in d:
    print("Yes,Model is one of the key in dict")
print("----------------------------------")
print(len(d))
print("----------------------------------")
D={223:"jimmy",120:"Alex",4j:"mike"}#4j is compelx_number
print(D)
