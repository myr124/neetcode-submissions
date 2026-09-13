class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedList = sorted(nums)
        print(sortedList)
        consecutiveList = defaultdict(int)
        key = 0
        prev = 0
        for i in sortedList:
            if not consecutiveList:
                if consecutiveList[key] is None:
                    consecutiveList[key]=1
                consecutiveList[key]+=1
                prev = i
                
            elif consecutiveList[key] is None:
                consecutiveList[key]=1
                prev = i
                
            elif i == prev+1:
                consecutiveList[key]+=1
                prev = i
            elif i==prev:
                continue
            else:
                key+=1
                prev = i
                consecutiveList[key] = 1
        maxLen = 0
        print(consecutiveList)
        for i in consecutiveList.keys():
            if consecutiveList[i] > maxLen:
                maxLen = consecutiveList[i]
        print(maxLen)
        return maxLen
        