class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if citations==[0] or citations==[0,0] or citations==[0,0,0]:
            return 0
        citations.sort()
        n=len(citations)
        for i in range(0,n):
            if(citations[i]>=n-i):
                return n-i