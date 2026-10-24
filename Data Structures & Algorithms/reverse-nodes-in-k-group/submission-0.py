class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the kth node in the current group
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next  # Fewer than k nodes remain

            group_next = kth.next

            # Reverse the group
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # group_prev.next was the old first node,
            # which is now the tail of the reversed group
            old_group_start = group_prev.next
            group_prev.next = kth
            group_prev = old_group_start