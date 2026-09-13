class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        
        for i in nums:
            if res[i] == None:
                res[i] = 1
            else:
                res[i] += 1
            
        buckets = {key:[] for key in range(len(nums)+1)}
        print(res)
        print(buckets)
        for key in res.keys():
            if res[key] in buckets.keys():
                buckets[res[key]].append(key)
        mostfreq = []
        print(buckets)
        for bucket in list(buckets.keys())[::-1]:
           
            for val in buckets[bucket]:
                mostfreq.append(val)
                if len(mostfreq)== k:
                    return mostfreq


# Can use a list for buckets instead of a dictionary