class Solution:
    def maximumValue(self, s: List[str]) -> int:
        maxcount=0
        for i in s:
            if i.isalpha():#dont need
                maxcount=max(maxcount,len(i))
            elif i.isdigit():
                maxcount=max(maxcount,int(i))
            else:
                maxcount=max(maxcount,len(i))
        return maxcount