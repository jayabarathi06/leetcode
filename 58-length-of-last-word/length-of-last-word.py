class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n=s.strip()
        a=s.split()
        b=a[-1]
        return len(b)
        if s=="":
            return 0