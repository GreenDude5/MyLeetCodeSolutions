class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == "-":
            a = int(f"-{str(x)[:0:-1]}")
            if a not in range(-2**31,(2**31)-1):
                return 0
            return a
        elif str(x)[0] == 0:
            a = int(str(x)[:1:-1])
            if a not in range(-2**31,(2**31)-1):
                return 0
            return a
        else: 
            a = int(str(x)[::-1])
            if a not in range(-2**31,(2**31)-1):
                return 0
            return a