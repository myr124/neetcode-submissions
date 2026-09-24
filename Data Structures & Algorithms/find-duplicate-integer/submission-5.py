class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        dup = set()
        
        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        print(slow)
        slow2 = 0

        while slow2!=slow:
            slow2 = nums[slow2]
            slow = nums[slow]

        
        return slow
