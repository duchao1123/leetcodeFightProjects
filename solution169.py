"""
169. 多数元素

给定一个大小为 n 的数组 nums ，返回其中的多数元素。
多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：nums = [3,2,3]
输出：3
"""

"""
思路：
数量大于列表总数量一半的元素，证明最多只能有一个
遍历1/2列表，如果那个元素的count > len(num) / 2 积满足条件返回
"""


class Solution(object):

    def majorityElement(self, nums: list) -> int:
        hf_size = int(len(nums) / 2)
        for e in nums[:hf_size]:
            if nums.count(e) > hf_size:
                return e
        return -1  # 不存在


if __name__ == "__main__":
    print(Solution().majorityElement([3, 2, 3]))
    print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
