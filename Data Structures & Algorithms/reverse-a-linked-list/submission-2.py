# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
reverse a linked list
challenges:
when we switch pointers we end up losing info on next pointer


curr = current pointer
tmp = curr.next
curr.next = prev
prev = curr
curr = tmp
before we swap we need to store next pointer somewhere
1->2->3
1<-2? 3

'''




class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        return prev
            

        
        