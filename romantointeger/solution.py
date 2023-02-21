class Solution:
    encoding = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}
    
    def roman_to_int(self, s):
        res = 0
        decoded = [self.encoding[i] for i in s]
        for i in range(len(decoded) - 1):
            if decoded[i + 1] > decoded[i]:
                res -= decoded[i]
            else:
                res += decoded[i]
        res += decoded[-1]
        
        return res