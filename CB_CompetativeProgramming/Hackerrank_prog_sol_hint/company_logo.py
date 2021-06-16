# task is to find the top three most common characters in the string.

# Print the three most common characters along with their occurrence count.
# Sort in descending order of occurrence count.
# If the occurrence count is the same, sort the characters in alphabetical order.

from collections import Counter


s = input()
s = ''.join(sorted(s))
print(s)
w = Counter(s).most_common(3)
for _ in w:
    print(f"{_[0]} {_[1]}")


