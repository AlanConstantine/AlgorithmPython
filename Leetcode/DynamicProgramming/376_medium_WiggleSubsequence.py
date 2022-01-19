# -*- coding: utf-8 -*-
# @Author: Alan Lau
# @Date: 2022-01-19 17:11:05

# 如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 摆动序列 。第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。

# 例如， [1, 7, 4, 9, 2, 5] 是一个 摆动序列 ，因为差值 (6, -3, 5, -7, 3) 是正负交替出现的。

# 相反，[1, 4, 7, 2, 5] 和 [1, 7, 4, 5, 5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
# 子序列 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。

# 给你一个整数数组 nums ，返回 nums 中作为 摆动序列 的 最长子序列的长度 。

#  

# 示例 1：

# 输入：nums = [1,7,4,9,2,5]
# 输出：6
# 解释：整个序列均为摆动序列，各元素之间的差值为 (6, -3, 5, -7, 3) 。
# 示例 2：

# 输入：nums = [1,17,5,10,13,15,10,5,16,8]
# 输出：7
# 解释：这个序列包含几个长度为 7 摆动序列。
# 其中一个是 [1, 17, 10, 13, 10, 16, 8] ，各元素之间的差值为 (16, -7, 3, -3, 6, -8) 。
# 示例 3：

# 输入：nums = [1,2,3,4,5,6,7,8,9]
# 输出：2
#  

# 提示：

# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
#  

# 进阶：你能否用 O(n) 时间复杂度完成此题?

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/wiggle-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution1:
    def wiggleMaxLength(self, nums) -> int:
        size = len(nums)
        if size < 2:
            return size
        up = [1] * size  # up存储以i结尾时最长上升摆动长度
        down = [1] * size  # down存储以i结尾时最长下降摆动长度
        for i in range(1, size):
            if nums[i] > nums[i-1]:
                # 当元素上升时,当前下标的up的值来自down[i-1] + 1转移,这样才满足摆动,或者也来自于前一个下标的up结果,
                # 即对于一个下标i,它的最长上升摆动长度在nums[i] > nums[i-1]断开了,所以可以直接记录up[i-1]
                up[i] = max(up[i-1], down[i-1] + 1)
                down[i] = down[i-1]  # 因为元素上升,所以down的记录和前一个元素一致
            elif nums[i] < nums[i-1]:
                down[i] = max(down[i-1], up[i-1] + 1)
                up[i] = up[i-1]
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]
        return max(up[-1], down[-1])


class Solution:
    # 优化空间
    def wiggleMaxLength(self, nums) -> int:
        size = len(nums)
        if size < 2:
            return size
        up = 1
        down = 1
        for i in range(1, size):
            if nums[i] > nums[i-1]:
                up = max(down+1, up)
            elif nums[i] < nums[i-1]:
                down = max(up+1, down)
            else:
                continue
        return max(up, down)
 # refer to: https://leetcode-cn.com/problems/wiggle-subsequence/solution/bai-dong-xu-lie-by-leetcode-solution-yh2m/


nums = [1, 7, 4, 9, 2, 5]
nums = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(Solution().wiggleMaxLength(nums))
