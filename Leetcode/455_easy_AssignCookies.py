# 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

# 对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。
# 如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。
# 你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

#  
# 示例 1:

# 输入: g = [1,2,3], s = [1,1]
# 输出: 1
# 解释:
# 你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
# 虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
# 所以你应该输出1。


class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        child = 0
        coolkies = 0
        g = sorted(g)
        s = sorted(s)
        while child < len(g) and coolkies < len(s):
            if g[child] <= s[coolkies]:
                child += 1
            coolkies += 1
        return child


g = [10, 9, 8, 7]
s = [5, 6, 7, 8]
print(Solution().findContentChildren(g, s))
