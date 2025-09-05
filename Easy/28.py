class Solution:
    def strStr(seld, haystack: str, needle: str) -> int:
        if not needle in haystack:
            return -1
        return haystack.index(needle)