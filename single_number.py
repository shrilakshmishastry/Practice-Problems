# Given a non-empty array of integers, every element appears
 # twice except for one. Find that single one.

word = input()
word = word.strip("[]").split(",")
print(word)
s = Solution
d = dict()
for i in word:
    i = int(i)
    d[i] = d.get(i,0)+1
values = list(d.values())
keys = list(d.keys())

print(keys[values.index(1)])
