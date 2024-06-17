def solution(nums1, nums2):
    # simulate merging by creating left partition based on endpoints
    # start with left partition equal up to midpoint of larger list + first elements of second list up to half_size
    # fix partition so that both left endpoints are <= the opposite right start point
    # no need to check if left endpoints are <= right endpoint of the same list since they are given sorted

    total_size = len(nums1) + len(nums2)
    half_size = total_size // 2

    if len(nums1) > len(nums2):
        i1 = len(nums1) // 2
        i2 = half_size - i1 - 2
    else:
        i2 = len(nums2) // 2
        i1 = half_size - i2 - 2

    l1 = nums1[i1] if 0 <= i1 < len(nums1) else (float('inf') if i1 >= len(nums1) else float('-inf'))
    l2 = nums2[i2] if 0 <= i2 < len(nums2) else (float('inf') if i2 >= len(nums2) else float('-inf'))
    r1 = nums1[i1 + 1] if 0 <= i1 + 1 < len(nums1) else (float('inf') if i1 + 1 >= len(nums1) else float('-inf'))
    r2 = nums2[i2 + 1] if 0 <= i2 + 1 < len(nums2) else (float('inf') if i2 + 1 >= len(nums2) else float('-inf'))

    while not (l1 <= r2 and l2 <= r1):
        if l1 > r2:
            i1 -= 1
            i2 += 1
        if l2 > r1:
            i2 -= 1
            i1 += 1
        l1 = nums1[i1] if 0 <= i1 < len(nums1) else (float('inf') if i1 >= len(nums1) else float('-inf'))
        l2 = nums2[i2] if 0 <= i2 < len(nums2) else (float('inf') if i2 >= len(nums2) else float('-inf'))
        r1 = nums1[i1 + 1] if 0 <= i1 + 1 < len(nums1) else (float('inf') if i1 + 1 >= len(nums1) else float('-inf'))
        r2 = nums2[i2 + 1] if 0 <= i2 + 1 < len(nums2) else (float('inf') if i2 + 1 >= len(nums2) else float('-inf'))

    if total_size % 2 == 0:
        return (max(l1, l2) + min(r1, r2)) / 2
    else:
        return min(r1, r2)