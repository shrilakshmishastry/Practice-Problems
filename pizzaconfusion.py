# Joey loves to eat Pizza. But he is worried as the
# quality of pizza made by most of the restaurants is
# deteriorating. The last
# few pizzas ordered by him did not taste good :(.
# Joey is feeling extremely hungry and wants to eat pizza.
 # But he is confused about the restaurant from where he should order. As always he asks Chandler for help.
#
# Chandler suggests that Joey should give each
# restaurant some points, and then choose the restaurant having maximum points. If more than one restaurant has same points, Joey can choose the one with lexicographically smallest name.
#
# Joey has assigned points to all the restaurants, but can't figure out which restaurant satisfies Chandler's criteria. Can you help him out?

# Write your code here
n = int(input())
d = dict()
for i in range(0,n):
    k,v = input().split(" ")
    v = int(v)

    d[k] = v

v = list(d.values())

v.sort()
m = max(v)

count = 0
vl = []
for i in d:

    if m == d[i]:
        count = count+1
        vl.append(i)
if(count==1)        :
    print(vl[0])
else:
    vl.sort()
    print(vl[0])
