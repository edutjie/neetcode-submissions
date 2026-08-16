class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_mul = 1
        zero_count = 0
        for i, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            else:
                total_mul *= num
        total_mul = int(total_mul)

        results = []
        for i, num in enumerate(nums):
            if num == 0:
                if zero_count-1 > 0:
                    results.append(0)
                else:
                    results.append(total_mul)
            else:
                if zero_count > 0:
                    results.append(0)
                else:
                    results.append(int(total_mul/num))

        return results


