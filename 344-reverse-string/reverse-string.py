class Solution:
    def reverseString(self, s: List[str]) -> None:
        left=0
        right=len(s)-1
        while(left<right):
            temp=s[right]
            s[right]=s[left] #without using third variable s[l],s[r]=s[l],s[r]
            s[left]=temp
            right-=1
            left+=1
        return s
        
        