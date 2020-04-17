 # Given a string containing only three types of characters: '(', ')'
 #  and '*', write a function to check whether this string is valid.
 #   We define the validity of a string by these rules:
 #
 #    1.Any left parenthesis '(' must have a corresponding right parenthesis ')'.
 #    2.Any right parenthesis ')' must have a corresponding left parenthesis '('.
 #    3.Left parenthesis '(' must go before the corresponding right parenthesis ')'.
 #    4.'*' could be treated as a single right parenthesis ')' or a single left
 #    parenthesis '(' or an empty string.
 #    5.An empty string is also valid.


s1 = input()
s2 = list(s1)


s = []
star = []

if (len(s1)==0 or s1 == "*" ):
    print("True")

elif (len(s1) == 1)    :
    print("False")
for i in range(0,len(s2)):
    print(i)
    if(s2[i] == "("):
        s.append(i)
    elif(s2[i]=="*")    :
        star.append(i)
    elif(s2[i]==")")    :
        if (len(s)>0):
            s.pop()
        elif(len(star)>0)    :
            star.pop()
        else:print(False)
print(s,star)
while (len(s) and len(star)):
    if s[-1] <star[-1]:
        s.pop()
        star.pop()
    else:
        print(False)
print(len(s)==0)
