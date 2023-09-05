class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        flag = False
        for idx in range(len(s)):
            if flag:
                flag = False
                continue
            if s[idx] not in ["I", "X", "C"]:
                result += roman_map[s[idx]]
            elif s[idx] in ["I", "X", "C"] and idx < len(s) - 1 and s[idx + 1] != s[idx]:
                if s[idx] == "I" and (s[idx + 1] == "V" or s[idx + 1] == "X"):
                    result += roman_map[s[idx + 1]] - roman_map[s[idx]]
                    flag = True
                    continue
                elif s[idx] == "X" and (s[idx + 1] == "L" or s[idx + 1] == "C"):
                    result += roman_map[s[idx + 1]] - roman_map[s[idx]]
                    flag = True
                    continue
                elif s[idx] == "C" and (s[idx + 1] == "D" or s[idx + 1] == "M"):
                    result += roman_map[s[idx + 1]] - roman_map[s[idx]]
                    flag = True
                    continue
                result += roman_map[s[idx]]
            else:
                result += roman_map[s[idx]]
        return result

sol = Solution()
print(sol.romanToInt("MCMXCIV"))