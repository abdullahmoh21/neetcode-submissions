class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        needs = [[] for _ in range(numCourses)]
        for course, req in prerequisites:
            needs[course].append(req)
        
        res = []
        state = defaultdict(int)    # 1 = resolving, 2 = taken, 0 = untouched
        def dfs(course):
            if state[course] == 2:
                return True

            state[course] = 1
            for r in needs[course]:
                if state[r] == 1:
                    return False
           
                if not dfs(r):
                    return False

            state[course] = 2
            res.append(course)
            return True
        
        for c, r in enumerate(needs):
            if not dfs(c):
                return []
        
        return res
                
            
            
