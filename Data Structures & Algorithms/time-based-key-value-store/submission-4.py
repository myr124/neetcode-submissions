class TimeMap:

    def __init__(self):
        self.keys = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append((timestamp,value))

        

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keys.get(key,[])
        l = 0
        r = len(values) - 1

        while l<= r:
            m = (l+r) // 2

            if timestamp < values[m][0]:
                r = m - 1
            elif timestamp >= values[m][0]:
                res = values[m][1]
                l = m + 1
        
        return res

        
