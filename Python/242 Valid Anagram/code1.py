def solution(s, t):
    if len(s) != len(t): return False

    s_letters = {}
    for letter in s:
        if letter not in s_letters: s_letters[letter] = 1
        else: s_letters[letter] += 1

    for letter in t:
        if letter not in s_letters: return False
        s_letters[letter] -= 1
        if s_letters[letter] < 0: return False

    return True

