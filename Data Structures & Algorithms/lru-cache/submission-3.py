class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.cache = dict()
        self.capacity = capacity
        self.history = []

    def get(self, key: int) -> int:
        if key in self.cache:
            if key in self.history:
                self.history.remove(key)
            self.history.append(key)
            return self.cache[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            if key in self.history:
                self.history.remove(key)
            self.history.append(key)
            return

        if self.size >= self.capacity:
            if self.history:
                to_del = self.history.pop(0)
                if to_del in self.cache:
                    del self.cache[to_del]
                    self.size -= 1
                    if to_del in self.history:
                        self.history.remove(to_del)
        self.cache[key] = value
        self.size += 1

        if key in self.history:
            self.history.remove(key)
        self.history.append(key)



