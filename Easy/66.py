class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = "".join(map(str, digits))
        x = int(x) + 1
        return [int(i) for i in str(x)]