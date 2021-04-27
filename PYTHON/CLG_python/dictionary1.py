import operator
WordsFreqDict={"Hello":56,"at":26,"XX":99,"utest":43,"this":43}
print(WordsFreqDict)
sorted_x=sorted(WordsFreqDict.items(),key=operator.itemgetter(1))
print(sorted_x)
sorted_y=sorted(WordsFreqDict.items(),key=operator.itemgetter(1),reverse=True)
print(sorted_y)

