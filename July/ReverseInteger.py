class Solution:
    def reverse(self, x: int) -> int:
        rev = 0     
        if x < 0:
            n = -x   
            while (n > 0):
                a = n % 10
                rev = rev * 10 + a
                n = n // 10
            rev = -rev
        else:
            n = x
            while (n > 0):
                a = n % 10
                rev = rev * 10 + a
                n = n // 10
        if abs(rev) > 2**31:
            rev = 0
        return (rev)
    