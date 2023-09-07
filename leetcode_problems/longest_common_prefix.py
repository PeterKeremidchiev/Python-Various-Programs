class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        word = strs.pop()
        for el in strs:
            for i in range(len(word)):
                if word[:i + 1] != el[:i + 1]:
                    word = word[:i]
                    break
        return word

sol = Solution()
print(sol.longestCommonPrefix(["dog","racecar","car"]))