# Given an array of strings, group anagrams together.
l = map(str,input().strip(" ").split())
l = list(l)
word_list = list()

for k in l:
    if k == "":
        word = " "
    word = sorted(list(k))

    d = dict()
    for i in word:
        if i == "":
            d[""] = d.get(i,0)+1
        else:
            d[i] = d.get(i,0)+1
    word_list.append(d)
print(word_list)
a = dict()
for (k,o) in zip(word_list,l):
    print(k,o)
    print("k index",word_list.index(k))
    a[o] = [o]
    for j in range(l.index(o)+1,len(word_list)):
        print(j)
        if(list(word_list[j].values())== list(k.values()) and (list(word_list[j].keys()) == list(k.keys()))):
            a[o].append(l[j])
print(a)

for k in list(a.values()):
    if len(k)>1:
        for j in range(1,len(k)):
            if k[j] in a:
                print("true")
                del a[k[j]]
print(list(a.values()))
