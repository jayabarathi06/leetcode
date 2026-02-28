class Solution:
    def fib(self, n: int) -> int:
        if n==1:
            return 1
        if n==0:
            return 0
        i=self.fib(n-1)
        j=self.fib(n-2)
        return i + j
    
