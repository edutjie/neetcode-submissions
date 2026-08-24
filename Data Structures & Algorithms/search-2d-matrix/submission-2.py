class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        mid = 0
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                break
        ll, rr = 0, len(matrix[mid])-1
        while ll <= rr:
            mid2 = (ll + rr) // 2
            if target < matrix[mid][mid2]:
                rr = mid2 - 1
            elif target > matrix[mid][mid2]:
                ll = mid2 + 1
            else:
                return True

        return False