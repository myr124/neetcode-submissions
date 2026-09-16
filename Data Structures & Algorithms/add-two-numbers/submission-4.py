# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0
        dummy = ListNode()

        num = dummy

        while l1 or l2:
            if not l1:
                val = l2.val + carry
                num.next = ListNode(val%10)
                carry = val//10
            elif not l2:
                val = l1.val + carry
                num.next = ListNode(val%10)
                carry = val//10
            else:
                val = l1.val + l2.val + carry
                num.next = ListNode((val%10))
                carry = val // 10

            num = num.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if carry:
            num.next = ListNode(carry)
        
        return dummy.next
                
        