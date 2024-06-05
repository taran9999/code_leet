def solution(s):
    left = 0
    right = 0
    longest = 0

    chars = set()
    while right < len(s):
        while s[right] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[right])
        longest = max(longest, right - left + 1)
        right += 1

    return longest
