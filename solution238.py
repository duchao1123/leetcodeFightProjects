"""
238. 除自身以外数组的乘积

给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。
题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
请不要使用除法，且在 O(n) 时间复杂度内完成此题。

示例 1:
输入: nums = [1,2,3,4]
输出: [24,12,8,6]

示例 2:
输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]


"""


class Solution(object):

    def productExceptSelf(self, nums: list) -> list:
        total = 1
        for i in range(len(nums)):
            total *= nums[i]
        answer = [int(total / value) for value in nums]
        return answer

    def productExceptSelfOfficial(self, nums: list) -> list:
        l = [0] * len(nums)
        # 索引为0，不存在左边元素， =1
        l[0] = 1
        for i in range(1, len(nums)):
            # 从1开始
            l[i] = nums[i - 1] * l[i - 1]
        # print(l)

        r = [0] * len(nums)
        r[len(nums) - 1] = 1
        index = len(nums) - 2
        while index >= 0:
            r[index] = nums[index + 1] * r[index + 1]
            index -= 1
        # print(r)

        answer = []
        for i in range(len(nums)):
            answer.append(l[i] * r[i])

        return answer

    def productExceptSelfOfficial_1(self, nums: list) -> list:
        """
        再次优化，移除lr，将结果直接赋值与answer，减少空间占用
        """
        length = len(nums)
        answer = [0] * length

        # 先赋值左
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        print(answer)

        # 再计算右，并得到结果
        index = length - 1
        r = 1
        while index >= 0:
            # answer = l * r
            answer[index] = answer[index] * r
            # new_r = e * old_r
            r *= nums[index]
            index -= 1

        return answer


if __name__ == "__main__":
    # print(Solution().productExceptSelfOfficial([1, 2, 3, 4]))
    print(Solution().productExceptSelfOfficial_1([1, 2, 3, 4]))
    # print(Solution().productExceptSelfOfficial([-1, 1, 0, -3, 3]))
    # print(Solution().productExceptSelf([1,2,3,4]))
