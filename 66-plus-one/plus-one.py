class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=0
        for i in range(0,len(digits)):
            res=res*10+digits[i]
        a=res+1
        result=[]
        while a>0:
            result.append(a%10)   
            a//=10               
        result.reverse()              
        return result

     