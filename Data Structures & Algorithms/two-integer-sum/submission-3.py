class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return indices i and J so in this when we add i + j = target and i should not be = j 
        hashMap = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[n] = i
        return
