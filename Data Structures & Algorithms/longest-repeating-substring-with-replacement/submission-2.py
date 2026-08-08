class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, res = defaultdict(int), 0
        l = maxF = 0
        r = 0
        while r < len(s):
            count[s[r]] += 1
            maxF = max(maxF, count[s[r]])
            length = r - l + 1
            if length - maxF > k:
                count[s[l]] -= 1
                l += 1
            r += 1
            res = max(res, r - l)

        return res
