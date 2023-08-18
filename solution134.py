"""
134. 加油站

在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。


示例 1：
输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。


思路：
cost = [3,4,5,1,2] 油耗
gas = [1,2,3,4,5]  油站总油量
没有思路，暴力解法
遍历每个站尝试，
存在关系： （剩余油量 >= 所需油量） + 可加入油量 = 新剩余油量
存在约束：  剩余油量 < 所需油量 则不满足
终止条件：  行驶站数 = len


开销：
时间复杂度：最大遍历次数 n * n = O（n^2）
空间复杂度：最大新建列表容量 O(n)
"""


class Solution(object):

    def canCompleteCircuit(self, gas: list, cost: list) -> int:
        end_steps = len(gas)
        results = []

        for start_step in range(end_steps):
            # 初始
            steps = 0
            current_index = start_step
            current_size = gas[current_index]
            while True:
                # 不满足，取消
                if cost[current_index] > current_size:
                    break
                # 继续行驶
                current_size -= cost[current_index]
                current_index += 1
                # 由于是环行，可能此时index可能越界, 获取真实索引
                current_index %= end_steps
                steps += 1

                # 到达终点
                if steps == end_steps:
                    results.append(start_step)
                    break

                # 未到终点，再次加油
                current_size += gas[current_index]

        if results:
            print(results)
            return results[0]
        else:
            return -1


if __name__ == "__main__":
    print(Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))


