class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for i in range(len(strs[0])):
            tmp = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != tmp:
                    return result
            result += tmp
        return result