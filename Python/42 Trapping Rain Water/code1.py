def solution(height):
    # water can be trapped in any area between elevations of the same size (includes when one endpoint is greater)
    # in other words, area between two elevations, with height according to the smaller one, unless it is 0

    # Two pointers, represent boundaries for each "valley", start together, second pointer continues until it finds an
    # endpoint elevation. Calculate total water area while also adding blocks in between to subtract at the end,
    # then add this sequence to total area and repeat

    # We split the list of heights at the rightmost index of the maximum height, and reverse the second part. We
    # do the above method separately on both of them and add the result. This is to prevent the issue of skipping
    # areas that come after the max value, since there is no possible endpoint elevation after the max value.

    def helper(height):
        if len(height) <= 2: return 0
        p1 = 0
        p2 = 1
        total_water = 0

        while p1 < p2 < len(height):
            blocks = 0  # blocks in the area of water to subtract
            while height[p2] < height[p1]:  # advance p2 until it finds an appropriate endpoint for p1
                blocks += height[p2]
                p2 += 1
                if p2 >= len(height): break
            total_water += 0 if p2 >= len(height) else min(height[p1], height[p2]) * (p2 - p1 - 1) - blocks
            p1 = p2
            p2 += 1

        return total_water

    right_max_index = len(height) - 1 - height[::-1].index(max(height))
    return helper(height[:right_max_index + 1]) + helper(height[right_max_index:][::-1])
