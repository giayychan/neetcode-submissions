class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nextTargetMap = {}
        i = 0
        while i < len(nums):
            nextTargetIndex = nextTargetMap.get(nums[i])
            if nextTargetIndex != None:
                return [nextTargetIndex, i]
            nextTarget = target - nums[i]
            nextTargetMap[nextTarget] = i
            i += 1
            
