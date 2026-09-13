# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        reverse = prev
        revHead = reverse
        prev = None
        k = 0
        while reverse:
            k+=1
            if k==n:
                nextNode = reverse.next
                reverse = prev
                if reverse != None:
                    reverse.next = nextNode
                else:
                    if nextNode:
                        revHead = nextNode
                        reverse = nextNode
                    else:
                        revHead = None
                        break
            prev = reverse
            reverse = reverse.next
        
        prev = None
        curr = revHead

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
        