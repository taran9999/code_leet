def solution(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] < target: left += 1
        elif numbers[left] + numbers[right] > target: right -= 1
        else: return sorted({left + 1, right + 1})
