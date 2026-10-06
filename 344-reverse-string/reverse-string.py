class Solution:
    def reverseString(self, s: List[str]) -> None:
        left=0
        right=len(s)-1
        while(left<right):
            temp=s[right]
            s[right]=s[left]
            s[left]=temp
            right-=1
            left+=1
        return s
        
        