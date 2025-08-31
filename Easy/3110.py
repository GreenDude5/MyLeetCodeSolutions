class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        tmp = s[0]
        for i in range(1, len(s)):
            char = s[i]
            if char == tmp:
                continue
            else:
                total += abs(ord(char) - ord(tmp))
                tmp = char
        return total
