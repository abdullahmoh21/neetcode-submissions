class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix) - 1
        while i < j:
            middle = (i + j) // 2
            if matrix[middle][-1] >= target:
                j = middle
            else:
                i = middle + 1

        if matrix[i][-1] < target:
            return False

        row = matrix[i]

        i, j = 0, len(row) - 1
        while i < j:
            middle = (i + j) // 2
            if row[middle] == target:
                return True
            elif row[middle] < target:
                i = middle + 1
            else:
                j = middle 
        return row[i] == target
