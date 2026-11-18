class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordList.append(beginWord)
        edges = defaultdict(list)
        for word in wordList:
            edges[word] = []
            for sub_word in list(edges.keys()):
                i = j = 0
                dif = 0
                while i < len(sub_word):
                    if word[i] != sub_word[i]:
                        dif += 1
                    i += 1
                    j += 1

                if dif != 1:
                    continue
           
                edges[word].append(sub_word)
                edges[sub_word].append(word)
        
        # start walking from startWord and see if we can get to endWord
        q = deque()
        visited = set(beginWord)
        q.append((beginWord, 0))
        depth = 1
        while q:
            node, depth = q.popleft()
            if node == endWord:
                return depth + 1

            for neigh in edges[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    q.append((neigh, depth + 1))
        
        return 0


        
            







        