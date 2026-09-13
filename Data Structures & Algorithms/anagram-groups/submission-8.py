
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        orderedDictionary = {i:sorted(i) for i in strs}
        sublistArray = []
        match = False
        for i in strs:
            match = False
            if not sublistArray:
                sublistArray.append([i])
            else:
                for e in sublistArray:
                    print (orderedDictionary[i] == orderedDictionary[e[0]])
                    if orderedDictionary[i] == orderedDictionary[e[0]]:
                        e.append(i)
                        match = True
                        continue
                if not match:
                    sublistArray.append([i])
                    


        return sublistArray
            