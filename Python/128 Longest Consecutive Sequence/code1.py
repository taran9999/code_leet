def solution(nums):

    # collect nums into a hash set for constant lookup time + number of occurrences doesn't matter
    nums_set = set()
    for num in nums: nums_set.add(num)
    max_length = 0 # counter variable for longest currently found sequence

    for num in nums_set:
        if num - 1 not in nums_set: # num is the start of a potential consecutive sequence
            seq_length = 0
            while num in nums_set:
                seq_length += 1
                num += 1
            if seq_length > max_length: max_length = seq_length

    return max_length

# Could also do a memoization type algorithm to avoid checking partial sequences multiple times. But since
# hash set has constant lookup time, the memory tradeoff may not be worth it.

