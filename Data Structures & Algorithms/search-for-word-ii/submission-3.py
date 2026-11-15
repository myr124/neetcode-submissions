'''
2d grid of characters board a list of strings words

return all words that are present in the grid


Input:
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],

o (k*(m*n))

words = ["bat","cat","back","backend","stack"]

Output: ["cat","back","backend"]


we make a prefix tree with a base trie node


'''


class TrieNode():
    def __init__(self):
        self.children = {}
        self.word = False


class Solution:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word:str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.addWord(word)
        
        rows = len(board)
        cols = len(board[0])

        res = set()

        visited = set()
        
        def dfs(r,c,cur,snapshot):
            if r < 0 or c < 0 or r == rows or c == cols or (r,c) in visited or board[r][c] not in cur.children:
                return
            
            
            visited.add((r,c))

            cur = cur.children[board[r][c]]

            snapshot+=board[r][c]
            if cur.word:
                res.add(snapshot)
                       
            
            dfs(r+1,c,cur,snapshot)
            dfs(r-1,c,cur,snapshot)
            dfs(r,c+1,cur,snapshot)
            dfs(r,c-1,cur,snapshot)

            visited.remove((r,c))

        
        for r in range(rows):
            for c in range(cols):
                cur = self.root
                if board[r][c] in cur.children:
                    dfs(r,c,cur,"")


        return list(res)



'''
["o","a","a","n"],
["e","t","a","e"],
["i","h","k","r"],
["i","f","l","v"]

'''
        