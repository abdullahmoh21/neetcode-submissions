class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        res = []
        i = 0
        j = 1
        while j < len(intervals):
            while j < len(intervals) and intervals[i][1] < intervals[j][0]:
                res.append(intervals[i])
                i += 1
                j += 1
            
            mergeInterval = intervals[i].copy()

            while j < len(intervals) and intervals[j][0] <= mergeInterval[1]:
                mergeInterval[0] = min(mergeInterval[0], intervals[j][0])
                mergeInterval[1] = max(mergeInterval[1], intervals[j][1])
                j += 1
            i = j
            res.append(mergeInterval)


        
        return res

