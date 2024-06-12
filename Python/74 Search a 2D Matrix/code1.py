def solution(matrix, target):
    for row in matrix:
        if row[0] <= target <= row[-1]:
            left = 0
            right = len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if target > row[mid]: left = mid + 1
                elif target < row[mid]: right = mid - 1
                else: return True
            return False
    return False
