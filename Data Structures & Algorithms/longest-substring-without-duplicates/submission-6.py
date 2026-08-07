class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chatSet, res = set(), 0
        left = 0

        for right, char in enumerate(s):
            while char in chatSet:
                chatSet.remove(s[left])
                left += 1
            chatSet.add(char)
            res = max(res, right - left + 1)
        
        return res