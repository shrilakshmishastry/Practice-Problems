# Given a string S consisting of uppercase and 
# lowercase characters. The task is to sort
# uppercase and lowercase letters separately such that
#  if the ith place in the original string had an
#   Uppercase character then it should not have a
#  lowercase character after being sorted
#  and vice versa.
import string
T = int(input())
for i in range(0,T):
    N = int(input())
    s = input()
    lowerCase={}
    upperCase = {}

    for k in range(0,N):

        if(s[k] in string.ascii_lowercase ):
            lowerCase[k]=ord(s[k])
        elif(s[k] in string.ascii_uppercase):
            upperCase[k]=ord(s[k])

    keys =list(lowerCase.keys())

    values = list(lowerCase.values())

    keys = sorted(keys)

    values = sorted(values)
    keysU = list(upperCase.keys())
    valuesU = list(upperCase.values())
    keysU = sorted(keysU)
    valuesU = sorted(valuesU)
    s = []
    for m  in range(0,len(keys)):
        s.insert(keys[m],chr(values[m]))

    for m in range(0,len(keysU)):
        s.insert(keysU[m],chr(valuesU[m]))
    print(''.join(s))
