class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord==endWord: return 0
        queue = [beginWord]
        depth = 1

        while queue and len(wordList):
            n = len(queue)
            for _ in range(n):
                leveled_child = queue.pop(0)
                neighbours = self.getNeighbors(leveled_child,wordList)
                if endWord in neighbours: return depth+1
                wordList = list( filter( lambda x: x not in neighbours, wordList))
                queue.extend(neighbours)
            depth += 1
        if len(wordList): return 0
        return depth
    
    def getNeighbors(self,word, wordlist):
        n = len(word)
        result = []
        for w in wordlist:
            diff = 0
            if len(w) != n: continue
            for i in range(n):
                if w[i]==word[i]: continue
                diff += 1
            if diff==1: result.append(w)
        return result
            