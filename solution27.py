"""
27. 移除元素

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

示例 1：
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，
而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
"""

'''
分析：
不额外创建数组空间，如果又重复数据，怎么处理？
从尾部删除，以至于未删除部分数组索引值不变
# 没有现成右删除内置函数，就用rfind，加remove，此时index为末尾匹配index
'''


class Solution(object):

    def removeElement(self, nums: list, val: int):
        for i in range(nums.count(val)):
            nums.remove(val)
        print(nums)
        return len(nums)

    def remove_element_official(self, nums: list, val: int):
        """
        官方给的方案：双指针
        left 为应插入索引
        right 为遍历索引
        """
        left = right = 0
        while right < len(nums):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            right += 1
        nums = nums[:left + 1]
        print(nums)
        return left


if __name__ == "__main__":
    list_values = [3, 2, 2, 3]
    e_value = 3

    list_values_1 = [0, 1, 2, 2, 3, 0, 4, 2]
    e_value_1 = 2

    # print(Solution().removeElement(list_values, e_value))
    print(Solution().remove_element_official(list_values, e_value))
    # print(Solution().removeElement(list_values_1, e_value_1))
    print(Solution().remove_element_official(list_values_1, e_value_1))




