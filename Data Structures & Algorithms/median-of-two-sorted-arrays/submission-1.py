'''
given two sorted arrays of size m and n
return median value among all elements of two arrays
brute force is simple we can just merge arrays and return the midpoint since theyre already sorted
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedList = nums1 + nums2
        mergedList.sort()
        print(mergedList)

        if len(mergedList) % 2 == 0:
            return (mergedList [(len(mergedList)//2)-1]+mergedList[len(mergedList)//2]) / 2
        return mergedList[len(mergedList)//2]
        