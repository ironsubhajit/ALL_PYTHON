a = [1, "hi", "python",2]
print(a[3:])
print(a[0:2])
print(a)
print(a + a)
print(a *3)
fruits=["apple","banana","cherry","apple","banana","cherry"]
print(fruits)
print(fruits[1])
fruits[1]="blackcurrent"
print(fruits)
for x in fruits:
    print(x)
if "apple" in fruits:
    print("yes,apple is in the fruits list")
print(len(fruits))
fruits.append("orange")
print(fruits)
fruits.insert(1, "orange")
print(fruits)
