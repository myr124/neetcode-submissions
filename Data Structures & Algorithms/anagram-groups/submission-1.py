class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupList=[]
        map= {i:sorted(i) for i in strs}
        completed = set()
        
        print(map)

        for i,n in enumerate(map):
            for j in strs:
                if(map[n]==map[j] and "".join(map[j]) not in completed):
                    groupList.append([])
                    groupList[i].append(j)
            completed.add("".join(map[n]))
            print(completed)        
            
        list2 = [x for x in groupList if x != []]           
                    

        return list2
        