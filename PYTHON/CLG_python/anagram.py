def is_anagram(str1, str2):
    str1="".join(sorted(str1.lower())).split()
    str2="".join(sorted(str2.lower())).split()
    if (str1 == str2):
        return(print("This is an anagram."))
    else:
        return(print("This is not an anagram!"))


str1=input("Enter the 1st string: ")
str2=input("Enter the 2nd input: ")
is_anagram(str1,str2)
