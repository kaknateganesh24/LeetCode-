# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
            count=0
            current=head
            while current!=None:
                count+=1
                current=current.next
            middle=count//2
            current=head
            for i in range((middle)):
                current=current.next
            return current



#        
        