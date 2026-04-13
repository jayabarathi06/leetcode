class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max=0
        for i in range(len(accounts)):
            current=0
            for j in range(len(accounts[i])):
                current+=accounts[i][j]
            if(current>max):
                 max=current      
        return max