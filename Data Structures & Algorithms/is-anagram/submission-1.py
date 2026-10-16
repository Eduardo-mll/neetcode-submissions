class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else: 
            count1 = {}
            count2 = {}
            for l1 in s:
                count1[l1] = count1.get(l1, 0) +1
            for l2 in t:
                count2[l2] = count2.get(l2, 0) +1

            return count1 == count2


        
        