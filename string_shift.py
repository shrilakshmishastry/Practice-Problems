# You are given a string s containing lowercase English letters,
#  and a matrix shift, where shift[i] = [direction, amount]:
#
# direction can be 0 (for left shift) or 1 (for right shift).
# amount is the amount by which string s is to be shifted.
# A left shift by 1 means remove the first character of s and append it to the end.
# Similarly, a right shift by 1 means remove the last character of s
#  and add it to the beginning.
#
# Return the final string after all operations.

s = input()
n = int(input("enter the no of manipulations"))
l = list()
for i in range(0,n):
    ele = [int(input()),int(input())]
    l.append(ele)

print(l,s)
for i in l:
    print(i)
    if(i[0]==0):
        s = s[i[1]:]+s[:i[1]]
        print(s)
    elif(i[0]==1)    :
        s = s[-i[1]:]+s[:-i[1]]
        print(s)
print(s)
