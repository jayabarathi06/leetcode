class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hLen=len(haystack)
        nLen=len(needle)       
        if nLen==0:
            return 0
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

       
       