class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmpNums = set(nums)
        k = len(tmpNums)
        nums[:] = sorted(tmpNums)
        return k