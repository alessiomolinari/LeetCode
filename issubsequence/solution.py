class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        
        if len(s) == 0 and len(t) == 0:
            return True
        
        if len(t) == 0:
            return False
    
        if len(s) == 0:
            return True
        i = 0
        j = 0
        while i < len(s):
            while s[i] != t[j]:
                j += 1
                if j >= len(t) and i < len(s):
                    return False
            i += 1
            j += 1
            if j >= len(t) and i < len(s):
                    return False
        return True
            