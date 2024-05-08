def solution(height):
    # Left and right pointer, move the pointer with a smaller line

    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        if area > max_area: max_area = area
        if height[right] > height[left]: left += 1
        else: right -= 1

    return max_area
