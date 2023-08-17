"""
45. 跳跃游戏 II

给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
0 <= j <= nums[i]
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

示例 1：
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

示例 2:
输入: nums = [2,3,0,1,4]
输出: 2


分析：
怎样能使跳跃最少？
每一步应该满足
range(index, index + [index] + 1) 范围内最大值，最差情况：【index + 1】= 【index】 + 1 即：step0 -> [index + 1]; step1 -> [index + 1 + [index + 1]]

"""


class Solution(object):

    def jump(self, nums: list) -> int:
        return self.found_min(0, nums)

    def found_min(self, index, nums: list):

        max_index = index + nums[index]
        count = 0
        # 最大跨步包含了终点索引，证明可以一步到达
        if max_index >= len(nums) - 1:
            count += 1
            return count

        # 最大跨步不包含了终点索引，证明需要寻找可跳范围内最大值，再次跳跃
        # 但是需要注意，范围内最大值 + 其索引 需要大于 起跳值 + 起跳索引， 否则所以内包含，不如使用【起跳 + 起跳索引】跳越
        tmp_max_value = index + nums[index]
        tmp_max_index = 0
        for i in range(index, max_index + 1):
            if index + i + nums[i] > tmp_max_value:
                tmp_max_value = nums[i]
                tmp_max_index = index + i

        # 步数计数：如果本步能够完成（上面if终结情况）返回步数1；如果本步内不能完成，+1本次步数，+递归进入到达终点所需的步数
        count += 1
        count += self.found_min(tmp_max_index, nums)
        return count


if __name__ == "__main__":
    print(Solution().jump([2, 3, 1, 1, 4]))
    print(Solution().jump([2, 3, 0, 1, 4]))
