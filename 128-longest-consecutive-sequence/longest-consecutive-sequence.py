class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(set(nums))
        l=[]
        c=1
        for i in range(1, len(nums)):
            if nums[i]==nums[i-1]+1:
                c+=1
            else:
                l.append(c)
                c=1
        l.append(c)
        return max(l)