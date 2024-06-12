def solution(nums):
    # choose the window where the left boundary is greater than the right boundary

    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]: left = mid + 1
        else: right = mid
    return nums[left]
