"""
55. 跳跃游戏
* 先可以先跳一步，也可以按照索引0的值跳
* 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
* 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
*
* 示例 1：
* 输入：nums = [2,3,1,1,4]
* 输出：true
* 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
*
* 示例 2：
* 输入：nums = [3,2,1,0,4]
* 输出：false
* 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标
"""


class Solution(object):

    def canJump(self, nums: list) -> bool:
        return self.func(0, len(nums), nums) or self.func(1, len(nums), nums)

    def func(self, index, length, list_value):
        if index > length - 1 or length - 1 < list_value[index] + index:
            return False
        elif length - 1 == list_value[index] + index:
            return True
        elif list_value[index] == 0:
            return False
        else:
            index += list_value[index]
            return self.func(index, length, list_value)


if __name__ == "__main__":
    num1 = [2, 3, 1, 1, 4]
    num2 = [3, 2, 1, 0, 4]
    print(Solution().canJump(num1))
    print(Solution().canJump(num2))
