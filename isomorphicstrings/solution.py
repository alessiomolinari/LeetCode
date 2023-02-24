class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        self.mapping = {}
        for i in range(len(s)):
            if not self.establish_mapping(s[i], t[i]):
                return False
        return True


    def establish_mapping(self, c1: str, c2: str) -> bool:
        if c1 in self.mapping:
            if self.mapping[c1] == c2 :
                return True
            else:
                return False
        else:
            if c2 in self.mapping.values():
                return False
            else:
                self.mapping[c1] = c2
                return True
