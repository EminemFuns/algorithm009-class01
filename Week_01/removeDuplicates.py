# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        双指针法
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1
# leetcode submit region end(Prohibit modification and deletion)