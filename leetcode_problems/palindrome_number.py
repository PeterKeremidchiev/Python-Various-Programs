class Solution(object):
    def isPalindrome(self, x):

        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

sol = Solution()
print(sol.isPalindrome(121))