# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = i+j+1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i = i-1
            else:
                nums1[k] = nums2[j]
                j = j-1
            k -= 1
        nums1[:j+1] = nums2[:j+1]


nums1 = [0]
nums2 = [1]
solution = Solution()
solution.merge(nums1, 0, nums2, 1)
print(nums1)
# leetcode submit region end(Prohibit modification and deletion)
