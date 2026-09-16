# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        rev = None 
        curr = head

        while curr:
            temp = curr.next
            curr.next = rev
            rev = curr
            curr = temp
        
        dummy = ListNode()
        dummy.next = rev

        count = 0
        curr = dummy
        while curr:
            if count == n-1:
                print(curr.val)
                curr.next = curr.next.next

            count+=1
            curr = curr.next
        
        rev = None
        curr = dummy.next

        while curr:
            temp = curr.next
            curr.next = rev
            rev = curr
            curr = temp
        
        return rev


        