def solution(piles, h):
    # ceil(a/b) is equivalent to (a+b-1) // b for integers

    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2
        hours = 0
        for p in piles: hours += (p + mid - 1) // mid
        if hours <= h: right = mid
        else: left = mid + 1
    return left
