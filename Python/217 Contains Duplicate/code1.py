def solution(nums):
    seen_numbers = set()
    for num in nums:
        if num not in seen_numbers: seen_numbers.add(num)
        else: return True
    return False