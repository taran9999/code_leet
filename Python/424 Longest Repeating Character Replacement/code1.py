def solution(s, k):
    # sliding window where we allow up to k of the non-majority character

    left = 0
    right = 0
    longest = 0
    char_counts = {}
    max_char = s[0]

    while left <= right < len(s):
        char_counts[s[right]] = char_counts.get(s[right], 0) + 1
        if char_counts[s[right]] > char_counts[max_char]: max_char = s[right]
        if (right - left + 1) - char_counts[max_char] > k:
            char_counts[s[left]] -= 1
            left += 1
        longest = max(longest, right - left + 1)
        right += 1

    return longest
