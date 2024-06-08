def solution(s1, s2):
    # sliding window in s2 where we check for all characters of s1

    s1_chars = {}
    for c in s1:
        s1_chars[c] = s1_chars.get(c, 0) + 1

    left = 0
    right = 0

    while left <= right < len(s2):
        if s2[right] in s1_chars and s1_chars[s2[right]] > 0:
            s1_chars[s2[right]] -= 1
            if sum(s1_chars.values()) == 0: return True
            right += 1
        elif left < right:
            if s2[left] in s1_chars: s1_chars[s2[left]] += 1
            left += 1
        else: right += 1

    return False
