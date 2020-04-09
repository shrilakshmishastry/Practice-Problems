# Given a non-empty, singly linked list with head node head, 
# return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Node:

    def __init__(self, dataVal=None):
        self.val = dataVal
        self.next = None

class SLinkedList:
    """docstring for ."""

    def __init__(self):
        self.headVal = None



    def getTheMid(self,positionVal,j)        :
        link1 = self.headVal
        for k in range(0,j+1):
            if(link1.val == positionVal):
                self.headVal = link1

            link1 = link1.next

        return self.headVal




class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        l = head
        list1 = SLinkedList()
        list1.headVal = head
        listNum = list1.headVal
        i =0
        while listNum is not None:
            i=i+1
            listNum = listNum.next

        if (int(i%2) == 0):
            position = int((i-1)/2)+1
        else :
            position = int((i-1)/2)

        listNum = list1.headVal
        for  j in range(0,i):
            if (j == position):
                positionVal = listNum.val
                break
            listNum = listNum.next

        ll = list1.getTheMid(positionVal,j)

        return ll
