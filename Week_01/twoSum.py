# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = dict()
        result[nums[0]] = 0
        for i in range(len(nums)-1):
            if (target-nums[i+1]) in result:
                return [result[target-nums[i+1]], i+1]
            else:
                result[nums[i+1]] = i+1

nums = [2, 7, 11, 15]
solution = Solution()
list_t = solution.twoSum(nums, 9)
print(list_t)
# leetcode submit region end(Prohibit modification and deletion)