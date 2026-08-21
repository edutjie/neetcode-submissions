class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for p, s in zip(position, speed):
            pos_speed.append((p, s, (target-p)/s))
        pos_speed.sort(key=lambda x: x[0], reverse=True)

        ref = pos_speed.pop(0)
        res = 1
        for p, s, step in pos_speed:
            if step > ref[-1]:
                res += 1
                ref = (p, s, step)

        return res




