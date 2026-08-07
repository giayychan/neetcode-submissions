class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp, res = {}, 0
        left = 0

        for right, char in enumerate(s):
            if char in mp:
                left = max(left, mp[char] + 1)
            mp[char] = right
            res = max(res, right - left + 1)
        
        return res