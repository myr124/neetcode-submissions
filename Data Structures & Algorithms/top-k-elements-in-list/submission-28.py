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
        no = 0
        print(buckets)
        for bucket in list(buckets.keys())[::-1]:
            if no ==k:
                break
            for val in buckets[bucket]:
                if no < k:
                    mostfreq.append(val)
                no+=1 

        return mostfreq
