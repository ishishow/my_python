class Solution:
    def sum_of_square(n):
        s = 0

        return s
    
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            s = 0
            while n > 0:
                a = n % 10
                s += a*a
                n //= 10
            n = s
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)