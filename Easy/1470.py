class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        shuffled = []
        for i in range(n):
            shuffled.append(nums[i])
            shuffled.append(nums[i + n])
        return shuffled
