class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord==endWord: return 0
        # graph = {}
        queue = [beginWord]
        depth = 1

        while queue and len(wordList):
            # print(wordList)
            # print(graph)
            n = len(queue)
            # depth += 1
            for _ in range(n):
                leveled_child = queue.pop(0)
                neighbours = self.getNeighbors(leveled_child,wordList)
                # print(neighbours)
                if endWord in neighbours: return depth+1
                wordList = list( filter( lambda x: x not in neighbours, wordList))
                # graph[leveled_child] = neighbours
                queue.extend(neighbours)
            # print(queue)
            depth += 1
        if len(wordList): return 0
        return depth
        # graph = {}
        # visited = set()
        # res = float('inf')
        # def buildGraph(word, wordList, depth):
        #     nonlocal res
        #     if len(wordList)==0: return 0
        #     if word in graph.keys(): return
        #     print(word,depth)
        #     neighbours_list = self.getNeighbors(word,wordList)
        #     neighbours = list( filter( lambda x: x not in visited, neighbours_list))
        #     wordList = list( filter( lambda x: x not in neighbours_list, wordList))
        #     visited.update(neighbours)
        #     graph[word] = neighbours
        #     print(graph)
        #     if endWord in neighbours:
        #         res = min(res,depth+1)
        #         return
        #     for nei in neighbours:
        #         buildGraph(nei, wordList, depth+1)
        #     return
        # visited.add(beginWord)
        # buildGraph(beginWord, wordList, 1)
        # return (0 if res==float('inf') else res)
    
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
            