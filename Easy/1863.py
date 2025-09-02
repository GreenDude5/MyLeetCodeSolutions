class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        total = 0
        n = len(nums)
        for i in range(1 << n):
            curr_xor = 0
            for j in range(n):
                if i & (1 << j):
                    curr_xor ^= nums[j]
            total += curr_xor
        return total