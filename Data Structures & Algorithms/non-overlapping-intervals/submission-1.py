class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        merged = []
        remove = 0

        for start, end in intervals:
            if not merged or start >= merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = min(merged[-1][1], end)

        return len(intervals) - len(merged)