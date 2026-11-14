'''

a b c d e f g h i j k

a -> 


search is pretty simple just traverse trie until we hit end of word if it doesnt exist return false

for dots

we look at neighbor and look for nodes that 

'''


class TrieNode:
    def __init__(self):
        # children array which holds trieNodes
        self.children = {}
        self.end = False
        


class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        

    def addWord(self, word: str) -> None:
        
        curr = self.trie
        
        for i,c in enumerate(word):
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True
        

    def search(self, word: str) -> bool:

        # for c in word:

        #     if c in curr.children:
        #         curr = curr.children[c]
        #     elif c == ".":
        #         keys = list(curr.children.keys())
        #         curr = curr.children[keys[0]]
        #     else:
        #         return False


        '''
        .ay
        ay
        '''


        def dfs(j, root):
            
            cur = root


            for c in range(j,len(word)):
                if word[c] == ".":
                    for child in cur.children.values():
                        if dfs(c+1,child):
                            return True
                    return False
                else:
                    if word[c] in cur.children:
                        cur = cur.children[word[c]]
                    else:
                        return False

            return cur.end
        
        return dfs(0,self.trie)
        
