"""
122. 买卖股票的最佳时机 II

给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
返回 你能获得的 最大 利润 。

示例 1：
输入：prices = [7,1,5,3,6,4]
输出：7
解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
     总利润为 4 + 3 = 7 。


思路：
与版本1最大的区别是，可以买多次，但是同时只能持有一只

版本1解法：
定义最小值，定义最大差，一次遍历，不断修正选择

min_value = 99999
max_diff = 0

for e in list:
   if e < min_value:
      min_value = e
   elif e - min_value > max_diff:
      max_diff = e - min_value


复杂度：
一次循环O(n)
常数个变量O(1)


"""


class Solution(object):

    def maxProfit(self, prices: list) -> int:
        min_value = 99999
        max_value = 0
        tmp_max_diff = 0
        max_diff = 0
        for e in prices:
            if e < min_value:
                min_value = e
            elif e > max_value:
                max_value = e
                tmp_max_diff = e - min_value
            else:
                # 第一次错误修正：当从波峰掉下后，本次数据赋值给最小值，成为新的最小值开始比较，否则就会丢掉一个元素
                min_value = e
                max_diff += tmp_max_diff
        # 第二次错误修正：如果是递增数据，不会出现新的波谷，所以需要将记录的临时最大值返回
        return max(max_diff, tmp_max_diff)


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([1, 2, 3, 4, 5]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
