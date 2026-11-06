class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) -1

        while left <= right:
            mid = left + (right - left)//2
            if matrix[mid][-1] < target:
                left = mid +1
            elif matrix[mid][0] > target:
                right = mid -1
            else: 
                l = 0
                r = len(matrix[mid])-1
                while l <= r:
                    mi = l + (r-l)//2
                    if matrix[mid][mi] == target :
                        return True
                    elif matrix[mid][mi] > target:
                        r = mi - 1
                    else:
                        l = mi + 1
                return False
        return False
            

        