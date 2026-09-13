# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


'''
 

'''


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head
        

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        

        prev = None
        second = slow.next
        slow.next = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        

        curr = head
        
        while prev:
            # hold next values
            currNext = curr.next
            prevNext = prev.next

            curr.next = prev
            prev.next = currNext

            curr = currNext
            prev = prevNext
            
        

            
        
