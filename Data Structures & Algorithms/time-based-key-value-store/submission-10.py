'''

Design a time-based key-value data structure 
that can store multiple values for the same key 
at different time stamps and retrieve the key's value at a 
certain timestamp.

hashmap
alice: [(1,happy)]
key: arr[tuple1,tuple2]
'''


class TimeMap:

    def __init__(self):
        self.keyValue = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyValue[key].append((timestamp,value))
        

 
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        l,r = 0, len(self.keyValue[key])-1
        

        '''
        [1,3,4]
        '''

        while l<=r:
            m = (l+r) // 2

            if self.keyValue[key][m][0] <= timestamp:
                res = self.keyValue[key][m][1]
                l = m+1
            elif self.keyValue[key][m][0] > timestamp:
                r = m-1
            
        
        return res


        
