class Solution:
    def isValid(self, word: str) -> bool:
        vowels = 'aeiou'
        nums = '0123456789'
        vow = False
        con = False
        if len(word) < 3: return False
        else:
            for c in word:
                c = c.lower()
                if c.isalpha():
                    if c in vowels: vow = True
                    else: con = True
                elif not c.isdigit(): return False
        return vow and con