class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0
        window.add(nums[l])
        r = l + 1
        
        while r < len(nums):
            if nums[r] in window:
                return True
            
            if abs(l-r) == k and r+1 < len(nums):
                window.remove(nums[l])
                l+=1
                window.add(nums[l])
                r+=1
                if nums[r] in window:
                    return True
            else:
                window.add(nums[r])
                r+=1
                
        

        return False
            
            