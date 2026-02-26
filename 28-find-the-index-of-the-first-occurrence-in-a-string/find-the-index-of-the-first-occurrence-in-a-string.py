class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hlen=len(haystack)
        nlen=len(needle)       
        if nlen==0:
            return 0
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1

       
       