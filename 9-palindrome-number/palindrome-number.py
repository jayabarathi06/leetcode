class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        sum=0
        if temp<0:
          return False
        while temp>0:
            d=temp%10
            sum=sum*10+d
            temp//=10
        if sum==x:
          return True
        else:
          return False
