class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=0
        result=""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                f=s[i:j]
                if f==f[::-1] and len(f)>l:
                    l=len(f)
                    result=f
        return result