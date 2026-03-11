class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        '''unique=[x for x in nums if nums.count(x)==1]
        return sum(unique)'''
        unique=0
        for x in (nums):
            if nums.count(x)==1: 
               unique+=x
        return unique