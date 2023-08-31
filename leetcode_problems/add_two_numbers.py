class Solution(object):
    def add_two_numbers(self, l1, l2):
        l1.reverse()
        l2.reverse()
        first_num = [''.join(str(num) for num in l1)]
        second_num = [''.join(str(num) for num in l2)]
        result = int(first_num[0]) + int(second_num[0])
        res = [int(x) for x in str(result)]
        res.reverse()
        return res

solution = Solution()
print(solution.add_two_numbers([2, 4, 3], [5, 6, 4]))