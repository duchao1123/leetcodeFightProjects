"""
189. 轮转数组

给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

示例 1：
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

思路：

"""


class Solution(object):

    '''
    python感觉有点作弊。。。。
    使用切片
    '''
    def rotate(self, nums: list, k: int) -> list:
        nums = nums[len(nums) - k:] + nums[:len(nums) - k]
        return nums

    def rotate_other(self, nums: list, k: int) -> list:
        new_nums = []
        for index in range(len(nums)):
            new_nums.insert((index + k) % len(nums), nums[index])
        return new_nums


if __name__ == "__main__":
    print(Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3))
    print(Solution().rotate([-1, -100, 3, 99], 2))

    print(Solution().rotate_other([1, 2, 3, 4, 5, 6, 7], 3))
    print(Solution().rotate_other([-1, -100, 3, 99], 2))
