class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
     a=s+s
     b=a[1:-1]
     if s in b:
        return True
     else:
        return False  

#bcabcabcabcabcabcabcab
