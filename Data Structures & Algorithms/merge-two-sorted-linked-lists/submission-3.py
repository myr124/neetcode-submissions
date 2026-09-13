# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
you are given heads of two sorted linked lists list1 and list2

    x
1 2 4

x
1


1 -> 2 -> 4


'''


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        temp = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            
            dummy = dummy.next

        if list1:
            dummy.next = list1
        elif list2:
            dummy.next = list2

        return temp.next

        