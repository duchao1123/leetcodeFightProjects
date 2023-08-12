"""
88. 合并两个有序数组

给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，
分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。
为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，
后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

示例 1：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
"""

# 解
'''
题目分析：
递增顺序数组 num1， 存在m个有效元素
递增顺序数组 num2， 存在n个有效元素
合并num2 到 num1 中，保持递增顺序

思路：
暴力处理
截取num1的前m个元素为新的数组new_num1，
截取num2的前n个元素为新的数组new_num2，
创建新数组大小为m+n， 遍历new_num1，内部遍历new_num2, 排序插入新的数组中

伪代码：
new_num1 = num1[:m]
new_num2 = num2[:n]

result = []
for e_1 in new_num1:
    for e_2 in new_num2:
        if e_2 <= e_1:
            result.append(e_2)
        else:
            break 
    result.append(e_1)
'''
num1 = [1, 2, 3, 0, 0, 0]
num2 = [2, 5, 6]
m = 3
n = 3
new_num1 = num1[:m]
new_num2 = num2[:n]
list_1_cur_index = 0
list_2_cur_index = 0


def solution():
    result = []
    for i in range(m + n):
        result.append(get_value())
    return result


def get_value():
    """
    双指针思路，添加数据移动指针
    """
    global list_1_cur_index
    global list_2_cur_index

    # list1遍历完成
    if list_1_cur_index >= len(new_num1):
        # list2不越界保证是 result总大小为 m+n
        cur_list_2_value = new_num2[list_2_cur_index]
        list_2_cur_index += 1
        return cur_list_2_value

    if list_2_cur_index >= len(new_num2):
        cur_list_1_value = new_num1[list_1_cur_index]
        list_1_cur_index += 1
        return cur_list_1_value

    # 取当前指针数据，进行比较，较小的插入结果集，并移动指针
    cur_list_1_value = new_num1[list_1_cur_index]
    cur_list_2_value = new_num2[list_2_cur_index]
    if cur_list_1_value <= cur_list_2_value:
        list_1_cur_index += 1
        return cur_list_1_value
    else:
        list_2_cur_index += 1
        return cur_list_2_value


"""
思路二：
利用排序方法
将俩个数组合并，然后排序
"""


class Solution(object):

    def merge(self, l1, lc1, l2, lc2):
        # 1、num1只有前m位为有效数字
        # 2、将num2赋值给num1 以m开始的数组，完成合并
        l1[lc1:] = l2[:lc2 + 1]
        l1.sort()
        print(l1)


if __name__ == "__main__":
    # print(solution())
    Solution().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)

"""
时间复杂度：
m+n次循环，每次循环取俩个值（列表取值o1）所以时间复杂读为o(m+n）

空间复杂读:
分片切出了俩个新的列表，空间是m+n，结果列表m+n，俩个指针2，所以结果为2(m+n+1)
"""


