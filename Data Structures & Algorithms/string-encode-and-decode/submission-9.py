# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         encodedStr = ""
#         for i in strs:
#             encodedStr+=str(len(i))
#             encodedStr+="#"
#             encodedStr+=i
#         return encodedStr


#     def decode(self, s: str) -> List[str]:
        # range = []
        # read = False
        # word = ""
        # decodedStr = []
        # count = 0
        # for c in s:
        #     print(c)
        #     if c.isnumeric():
        #         range.append(c)
        #     elif c == "#":
        #         read=True
        #     elif read==True:
        #         word+=c
        #         count+=1
        #         if count == int("".join(range)):
        #             count = 0
        #             decodedStr.append(word)
        #             read=False
        #             word = ""
        #             range = []

        # return decodedStr
class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res                


            
