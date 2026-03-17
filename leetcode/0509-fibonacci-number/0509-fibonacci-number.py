class Solution:
    def fib(self, n: int, cur=(0, 1)) -> int:
        if n == 0:
            return cur[0]
        
        if n == 1:
            return cur[1]
        
        return self.fib(n - 1, (cur[1], cur[0] + cur[1]))