class Solution:
    def Fibonacci_num(self, n):
        a,b =0,1
        for i in range(n):
            a,b = b,a+b
        return a
        
    def fib(self, n: int) -> int:
        if n ==1:
            return 1
        return self.Fibonacci_num(n-1) + self.Fibonacci_num(n-2)
        
        