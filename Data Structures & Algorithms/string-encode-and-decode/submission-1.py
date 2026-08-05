class Solution:
    delimiter = '*'
    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + self.delimiter + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != self.delimiter:
                j += 1
            length = int(s[i:j])
            start = j + 1
            res.append(s[start : start + length])
            i = start + length
    
        return res