# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        position = 0
        for i, e in enumerate(nums):
            if nums[i] != 0:
                nums[position], nums[i] = nums[i], nums[position]
                position += 1

# leetcode submit region end(Prohibit modification and deletion)