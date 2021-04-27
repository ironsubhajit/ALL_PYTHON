from collections import Counter
def word_count(fname):
	with open(fname)as f:
		return Counter(f.read().split())
print("Frequency of words present: ",word_count("dictionary2.py"))
