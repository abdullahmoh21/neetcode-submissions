import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()                                  # by start
        order = sorted(range(len(queries)), key=lambda i: queries[i])

        ans = [-1] * len(queries)
        heap = []                                         # (length, end)
        cur = 0
        n = len(intervals)

        for i in order:
            q = queries[i]

            # add every interval that has started by q
            while cur < n and intervals[cur][0] <= q:
                start, end = intervals[cur]
                heapq.heappush(heap, (end - start + 1, end))
                cur += 1

            # lazily drop intervals that ended before q
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                ans[i] = heap[0][0]

        return ans




        