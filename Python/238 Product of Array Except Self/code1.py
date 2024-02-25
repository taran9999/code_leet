def solution(nums):
    # Store the products of each prefix and each suffix
    prefix_products = {-1: 1}
    suffix_products = {len(nums): 1}

    for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
        prefix_products[i] = prefix_products[i - 1] * nums[i]
        suffix_products[j] = suffix_products[j + 1] * nums[j]

    answer = []
    # the answer for each element i is the prefix product of the previous element times the
    # suffix product of the next element
    for i in range(len(nums)):
        answer.append(prefix_products[i - 1] * suffix_products[i + 1])

    return answer

