class TimeMap:
    def __init__(self):
        self.kv = {}

    def set(self, key, value, timestamp):
        if key not in self.kv: self.kv[key] = []
        self.kv[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.kv: return ""
        left = 0
        right = len(self.kv[key]) - 1
        t = None

        while left <= right:
            mid = (left + right) // 2
            if self.kv[key][mid][0] == timestamp: return self.kv[key][mid][1]
            elif self.kv[key][mid][0] > timestamp: right = mid - 1
            else:
                t = mid
                left = mid + 1
        return "" if t is None else self.kv[key][t][1]
