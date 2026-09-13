class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {i:target-j for i,j in enumerate(nums)}
        numMapRev = {target-j:i for i,j in enumerate(nums)}
        print(numMap)
        print(numMapRev)
        for i in numMap.keys():
            if numMapRev.get(target-numMap.get(i))!= None and (i != numMapRev.get(target -numMap.get(i)) ):
                return [i,numMapRev.get(target -numMap.get(i))]
        