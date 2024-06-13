def solution(nums, target):
    # check if target is in sorted side or non-sorted side

    left = 0
    right = len(nums) - 1

    while nums[left] > nums[right]:
        mid = (left + right) // 2
        if nums[mid] == target: return mid

        if nums[mid] > nums[right]: # right side non-sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
                break
            else: left = mid + 1
        else: # left side non-sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
                break
            else: right = mid - 1

    # regular binary search
    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]: left = mid + 1
        elif target < nums[mid]: right = mid - 1
        else: return mid
    return -1
