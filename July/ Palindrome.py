class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_x = str(x)
        str_x = list(s_x)
        for i in range(len(str_x)//2):
            if not str_x[i] == str_x[len(str_x) - i - 1]:
                return False
        return True