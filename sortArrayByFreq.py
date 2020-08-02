#User function Template for python3
'''
	Task is to sort the elements according
	to the frequency of their occurence
	in the given array.

	Function Arguments: array a with size n.
	Return Type:Array, the sorted array

'''
def sortByFreq(a,n):
    #code here
    d = dict()
    for i in a:
        d[i] = d.get(i,0)+1
    values = set(d.values())
    keys = set(d.keys())

    values = list(values)

    values.sort(reverse=True)
    keys = list(keys)
    keys.sort()

    c=list()
    for i in values:
        for   j in keys:
            if d[j]==i:
                for k in range(0,i):
                    c.append(j)


    return c


#{
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        l = sortByFreq(a,n)
        print(*l)
# } Driver Code Ends
