# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    """
    第一次利用了切片的方式，但是发现不符合题目要求，空间复杂度不是O(1),在leetcode上找打了三次反转的方式，使用这种方式完成了作业
    """
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        nums[:] = nums[length-k:] + nums[0:length-k]

    def rotate1(self, nums, k):
        length = len(nums)
        k = k % length

        def swap(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        swap(0, length-1)
        swap(0, k-1)
        swap(k, length-1)
# leetcode submit region end(Prohibit modification and deletion)