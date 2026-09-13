# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast = head
        slow = head
        prev = None


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None


        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        rev = prev
        orig = head

        while rev:
            tmp1, tmp2 = orig.next,rev.next
            orig.next = rev
            rev.next = tmp1
            orig, rev = tmp1,tmp2


        