def solution(nums, k):
    counts = {}
    top_k = set()
    smallest_top_k_key = None

    for n in nums:
        if n not in counts: counts[n] = 0
        counts[n] += 1

        if smallest_top_k_key is None:
            smallest_top_k_key = n
            top_k.add(n)
        elif len(top_k) < k:
            top_k.add(n)
            smallest_top_k_key = min([num for num in top_k], key=counts.get)
        elif n not in top_k and counts[n] > counts[smallest_top_k_key]:
            top_k.remove(smallest_top_k_key)
            top_k.add(n)
            smallest_top_k_key = min([num for num in top_k], key=counts.get)
        else: smallest_top_k_key = min([num for num in top_k], key=counts.get)

    return list(top_k)
