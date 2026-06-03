class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = set()

        for num in nums:
            if num in found:
                return True
            found.add(num)
        return False
        

        
        #if nums == int:
            #continue:
        #while self.hasDuplicate == list(nums):
         #   return True
        #else:
         #   return False




        