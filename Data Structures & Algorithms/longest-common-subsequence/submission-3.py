'''
given two strings text1 and text2 return length of the longest
common subsequence between two strings if one exists other return 0


Input: text1 = "abcd", text2 = "abcd"

what are we trying to do
find as many characters that are common between the two
what are some solutions to this
we could take shorter string and iterate through
check if character exists in second string
then we increment
Output: 4
o(n*m)

we also have to account for positioning so solution above doesnt work
without modification
'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        res = 0

        dp = [[0]*(len(text2)+1)for i in range(len(text1)+1)]
        print(dp)

        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else: 
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        
        return dp[0][0]


        

        