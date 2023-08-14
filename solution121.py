"""
121. 买卖股票的最佳时机

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

思路：
sorted一个新的列表，然后获取最大元素，和最小元素，及其索引，满足最大值索引大于最小值索引的组合为解
"""
import time


def timer(func):
    def call_fun(list_p):
        pre = time.time()
        result = func(list_p)
        prd = time.time()
        total_time = prd - pre
        print(f'总耗时 = {total_time:.6f}s')
        return result
    return call_fun


@timer
def max_profit_official(prices: list) -> int:
    min_value = 9999
    max_diff = 0
    for e in prices:
        if e < min_value:
            min_value = e
        elif e - min_value > max_diff:
            max_diff = e - min_value
    return max_diff


@timer
def maxProfit(prices: list) -> int:
    sorted_prices = sorted(prices)
    min_index = max_index = 0
    min_value = max_value = 0
    for i in sorted_prices:
        if min_value == 0 or i < min_value:
            min_value = i
            min_index = prices.index(min_value)
            if min_index == len(prices) - 1:
                continue
            for j in prices[min_index + 1:]:
                if max_value == 0 or j > min_value and j > max_value:
                    max_value = j
                    max_index = prices.index(j)
    print(f'min_index = {min_index}, max_index = {max_index}')
    print(f'min_index = {min_value}, max_index = {max_value}')
    return max_value - min_value if max_value > min_value else 0


if __name__ == "__main__":
    print(maxProfit([7, 1, 5, 3, 6, 4]))              # 0.000035s
    print(maxProfit([7, 6, 4, 3, 1]))                 # 0.000009s
    print(max_profit_official([7, 1, 5, 3, 6, 4]))    # 0.000002s
    print(max_profit_official([7, 6, 4, 3, 1]))       # 0.000001s
