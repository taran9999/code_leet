def solution(nums):
    sorted_nums = sorted(nums)
    r = []

    # run 2 sum with input array sorted after fixing the first element
    for i in range(len(sorted_nums) - 2):
        if i > 0 and sorted_nums[i] == sorted_nums[i - 1]: continue
        target = -sorted_nums[i]
        left = i + 1
        right = len(sorted_nums) - 1
        while left < right:
            if sorted_nums[left] + sorted_nums[right] < target: left += 1
            elif sorted_nums[left] + sorted_nums[right] > target: right -= 1
            else:
                r.append([-target, sorted_nums[left], sorted_nums[right]])
                left += 1
                while left < right and sorted_nums[left] == sorted_nums[left - 1]: left += 1
    return r
