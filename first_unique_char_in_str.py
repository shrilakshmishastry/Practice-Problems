# Given a string, find the first non-repeating character in 
# it and return it's index. If it doesn't exist, return -1.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = list(s)
        print(l)
        d = dict()
        for i in l:
            d[i] = d.get(i,0)+1
        print(d)
        values = list(d.values())
        keys = list(d.keys())
        print(values)
        try :
            key = keys[values.index(1)]
            print(key)
            return l.index(key)

        except:
            return -1
