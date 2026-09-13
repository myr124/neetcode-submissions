from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)
        
        sortedList = list(element for element, value in res.most_common(k))
        no = 0
        
        
        return sortedList