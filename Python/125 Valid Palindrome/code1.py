def solution(s):
    left = 0
    right = len(s) - 1
    s = s.lower()
    while left < right:
        while left < len(s) and not s[left].isalnum(): left += 1
        while right >= 0 and not s[right].isalnum(): right -= 1
        if left >= right: break
        if s[left] != s[right]: return False
        left += 1
        right -= 1
    return True
