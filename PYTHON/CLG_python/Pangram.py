from string import ascii_lowercase

def pangram(str):
    if set(ascii_lowercase).issubset(str):
        print("this is a pangram.")
    else:
        print("this is not a pangram.")


#print(ascii_lowercase)
str=input("Enter the string: ")
pangram(str)
