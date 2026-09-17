class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(row):
            left = 0
            right = len(row) - 1

            while left <= right:
                mid = (left + right) // 2
                if target == row[mid]:
                    return True
                elif target < row[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return False

        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[0]) - 1]:
                return binary_search(matrix[mid])
            elif target < matrix[mid][0]:
                right = mid - 1
            else:
                left = mid + 1
        
        return False