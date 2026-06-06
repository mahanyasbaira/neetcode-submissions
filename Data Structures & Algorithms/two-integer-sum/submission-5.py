class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            count = {}
            for i, n in enumerate(nums):
                difference = target - n
                if difference in count:
                    return[count[difference], i]
                count[n] = i
            return
