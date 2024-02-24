def solution(strs):
    unique_words = {}
    for word in strs:
        if str(sorted(word)) in unique_words: unique_words[str(sorted(word))].append(word)
        else: unique_words[str(sorted(word))] = [word]

    sol = []
    for word in unique_words:
        sol.append(unique_words[word])

    return sol
