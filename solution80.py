"""
80. 删除有序数组中的重复项 II

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，
使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1：
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5,
并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。
"""

"""
思路：
双指针 + 重复计数
left: 当前指针位置； 待插入索引 = left + 1
right：遍历指针
dup_time: 记录重复次数
"""


class Solution:

    def removeDuplicates(self, nums: list) -> int:
        left = 0
        right = 1
        dup_time = 0
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
                dup_time = 0
            elif dup_time < 1:
                left += 1
                nums[left] = nums[right]
                dup_time += 1
            right += 1
        # 验证打印，提交时不应该有，切片会创建新新的列表，空间复杂度 != O(n)
        nums = nums[:left + 1]
        print(nums)
        return left + 1


if __name__ == "__main__":
    print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))

"""
时间复杂度：
n次循环，每次循环取俩个值（列表取值O1）所以时间复杂读为O(n）

空间复杂读:
空间O(1)
"""
