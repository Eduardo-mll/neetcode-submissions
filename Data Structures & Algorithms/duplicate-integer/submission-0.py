class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set(nums)

        print (len(nums))
        print(len(hs))
        return not(len(nums) == len(hs))
        

        
        

        
        
        
        