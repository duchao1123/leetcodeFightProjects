"""
274. H 指数

给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。
根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，
并且每篇论文 至少 被引用 h 次。如果 h 有多种可能的值，h 指数 是其中最大的那个。

示例 1：
输入：citations = [3,0,6,1,5]
输出：3
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。

示例 2：
输入：citations = [1,3,1]
输出：1


分析：
翻一下题目：
整数数组，获取数组长度范围内最值，最值满足有最多个元素值>=此最值

官方思路：
降序排序list，遍历, 判定 list【index】 > index 可以继续遍历，一直到条件不成立break，此时获取到的list【index】就是h
"""


class Solution(object):

    def hIndex(self, citations: list) -> int:
        citations.sort(reverse=True)
        # h 的取值范围就是list索引，索引跟着遍历递增即可
        h = index = 0
        while index < len(citations) and citations[index] > h:
            h += 1
            index += 1
        return h


if __name__ == "__main__":
    num1 = [1, 2, 3, 0, 0, 0]
    num2 = [2, 5, 6]
    print(Solution().hIndex([1, 2, 3, 0, 0, 0]))
    print(Solution().hIndex([2, 5, 6]))





