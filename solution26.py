"""
26. 删除有序数组中的重复项

给你一个 升序排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，
返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。
nums 的其余元素与 nums 的大小不重要。
返回 k 。

示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。
不需要考虑数组中超出新长度后面的元素。
"""


class Solution(object):

    def removeDuplicates(self, nums: list) -> int:
        """
        双指针方式
        left：为当前要插入索引
        right：为遍历索引
        与27题最大的区别是末尾插入，27题是末尾替换
        """
        left = 0
        right = 1
        while right < len(nums):
            # 判定数字对当前数字不同，需要插入
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
            right += 1
        nums = nums[:left + 1]
        print(nums)
        return left + 1


if __name__ == "__main__":
    nums1 = [1, 1, 2]
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

    print(Solution().removeDuplicates(nums1))
    print(Solution().removeDuplicates(nums2))


"""
时间复杂度：
一次遍历 O(n)
空间复杂度:
没有创建新的占用 O(1)
"""



