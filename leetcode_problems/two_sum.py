class Solution(object):
    def two_sum(self, nums, target):
        result = []
        for idx in range(len(nums)):
            for idx_2 in range(idx + 1, len(nums)):
                if nums[idx] + nums[idx_2] == target and idx != idx_2:
                    result.extend([idx, idx_2])
                    break
                else:
                    continue
        return result


solution = Solution()
print(solution.two_sum([3, 2, 4], 6))

