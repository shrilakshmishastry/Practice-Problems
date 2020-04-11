# Design a stack that supports push, pop, top, and 
# retrieving the minimum element in constant time.
#
#     push(x) -- Push element x onto stack.
#     pop() -- Removes the element on top of the stack.
#     top() -- Get the top element.
#     getMin() -- Retrieve the minimum element in the stack.


class minStack:
    stack = []
    def __init__(self):
        pass
    def push(self,ele):
        self.stack.append(ele)
        print(self.stack)
    def pop(self)    :
        self.stack.pop()
        print(self.stack)
    def getMin(self)    :
        return min(self.stack)
    def top(self)    :
        return self.stack[len(self.stack)-1]

l = map(int,input().strip().split())
l = list(l)
# print(l)
m = minStack()
m.stack = l
m.push(2)
m.pop()
print(m.getMin())
print(m.top())
print(m.stack)
