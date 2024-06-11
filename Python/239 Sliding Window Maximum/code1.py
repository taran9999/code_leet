import collections


def solution(nums, k):
    # monotonic decreasing deque

    deque = collections.deque()
    deque.append(nums[0])
    ptr = 1
    max_nums = []

    # scan the first window
    while ptr < k:

        # we don't care about anything less than the newest element
        while len(deque) > 0 and deque[-1] < nums[ptr]: deque.pop()
        deque.append(nums[ptr])
        ptr += 1

    # max num in the current window will be on the left
    max_nums.append(deque[0])

    # scan remaining windows, checking the left end of the window
    while ptr < len(nums):
        # check if the max number is at the left end of the current window
        if deque[0] == nums[ptr - k]: deque.popleft()

        while len(deque) > 0 and deque[-1] < nums[ptr]: deque.pop()
        deque.append(nums[ptr])

        max_nums.append(deque[0])

        ptr += 1

    return max_nums
