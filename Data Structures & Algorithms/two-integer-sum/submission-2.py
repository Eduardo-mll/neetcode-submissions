class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = {}
        j = 0
        for i in nums:
            
            diference = target - i
            if hs.get(diference) != None :
                return [hs[diference],j]

            else:
                hs[i] = j

            j += 1

            

 
            





            









        