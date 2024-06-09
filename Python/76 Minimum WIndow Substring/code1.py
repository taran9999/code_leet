def solution(s, t):

    t_chars = {}
    for c in t:
        t_chars[c] = t_chars.get(c, 0) + 1

    left = 0
    right = 0
    min_left = 0
    min_right = len(s) + 1

    # move left and right to first character in t
    while left < len(s):
        if s[left] in t: break
        left += 1
    if left == len(s): return ""  # no characters from t in s
    right = left

    # map to keep count of t-chars in current substring
    curr_t_chars = {}
    for c in t_chars.keys(): curr_t_chars[c] = 0
    curr_t_chars[s[left]] = 1

    while left <= right < len(s):
        # Check for valid substring
        valid_sub = True
        for c in t_chars:
            if curr_t_chars[c] < t_chars[c]:
                valid_sub = False
                break
        if valid_sub:
            if (right - left) < (min_right - min_left):
                min_left = left
                min_right = right
            # valid - try for a shorter substring by moving left pointer to next t-char
            # or move right pointer forward if they are at the same spot
            if left < right:
                curr_t_chars[s[left]] -= 1
                left += 1
                while s[left] not in curr_t_chars: left += 1
            else:
                right += 1
                while right < len(s) and s[right] not in curr_t_chars: right += 1
                if right >= len(s): break
                curr_t_chars[s[right]] += 1
        else:
            # invalid - get the next t-char by moving right forward
            right += 1
            while right < len(s) and s[right] not in curr_t_chars: right += 1
            if right >= len(s): break
            curr_t_chars[s[right]] += 1

    if min_right == len(s) + 1: return ""
    else: return s[min_left:min_right + 1]