class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        needs = defaultdict(list)
        for course, req in prerequisites:
            needs[course].append(req)
        
        state = defaultdict(int)    # 0 -> untouched, 1 -> resolving, 2 -> taken
        def dfs(course):
            reqs = needs[course]
            state[course] = 1 # resolving

            for r in reqs:
                if r not in needs:
                    state[r] = 2    # mark taken
                    continue
                elif state[r] == 2:
                    continue
                elif state[r] == 1:   # cycle detected
                    return False
                elif not dfs(r):
                    return False
            
            state[course] = 2
            return True
            
        for c, _ in needs.items():
            if not dfs(c):
                return False

        return True
        

