class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r, maxAmount = 0, len(heights) - 1, 0
        while l < r:
            amount = (r - l) * min(heights[l], heights[r])
            maxAmount = max(amount, maxAmount)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1   

        return maxAmount
