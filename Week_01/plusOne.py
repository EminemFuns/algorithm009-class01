# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        for i in range(length-1, -1, -1):
            result = digits[i] + 1
            if result == 10:
                digits[i] = 0
            else:
                digits[i] = result
                return digits
        digits.insert(0, 1)
        return digits

digits = [9]
solution = Solution()
solution.plusOne(digits)
print(digits)
# leetcode submit region end(Prohibit modification and deletion)