class TimeMap:

    def __init__(self):
        self.db = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.db[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.db[key]:
            return self.db[key][timestamp]
        ts_keys = sorted(list(self.db[key].keys()))
        l, r = 0, len(ts_keys) - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            # print(l, r, mid)
            if ts_keys[mid] <= timestamp:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        # print(ts_keys)
        # print(self.db[key])
        # print(r, ts_keys[r])
        if ans == -1:
            return ""
        return self.db[key][ts_keys[ans]]
            