# Given two strings S and T, return
# if they are equal when both are typed
# into empty text editors.# means a backspace character.
import itertools
s = input()
t = input()
s,t= list(s),list(t)
a=['#']
b=['#']
print(s,t)

for (k,l) in itertools.zip_longest(s,t):
    print(k,l)
    if(k!=None and k=='#'):
        if(a[-1]!='#'):
            a.pop()
        else:
            a.append('#')
    if(k!=None and k!='#')         :
        a.append(k)
    if(l!=None and l=='#'):
        if(b[-1]!='#'):
            b.pop()
        else:
            b.append('#')
    if(l!=None and l!="#")         :
        b.append(l)
a = list(filter(lambda a:a!='#',a))
b = list(filter(lambda a:a!='#',b))
print(a==b)
