#UMPIRE
# Understand
# Plan
# Implement

# Understand

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)
        sortedList = list()
        mostFrequent = list()
        i = float('-inf')
        index = 0
        print(res)
        # for key in res.keys():
        #     if res[key] > i:
        #         print("1st if")
        #         sortedList.insert(0,key)
        #         i = res[key]
        #     elif (res[key]>res[sortedList[index]]):
        #         print(res[key])
        #         print("2nd if")
        #         sortedList.insert(index,key)
        #         i = res[key]
        #     else:
        #         print("3rd if")
        #         sortedList.append(key)
        #         i = res[key]
        #         index = sortedList.index(key)
        no = 0
        # print(sortedList)
        print(list(res))
        sortedList = [element for element,count in res.most_common() ]
        for a in sortedList:
            if no == k:
                break
            no+=1
            mostFrequent.append(a)
        
        return mostFrequent
            
            