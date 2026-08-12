class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1

        countS = {}  
        have, want = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            char = s[r]
            countS[char] = countS.get(char, 0) + 1
            if char in countT and countS[char] == countT[char]:
                have += 1

            while have == want:
                length = r - l + 1
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = length
                
                countS[s[l]] -= 1

                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if resLen != float('inf') else ""
