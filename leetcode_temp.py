class Solution(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        self.new_num1 = nums1[:m]
        self.new_num2 = nums2[:n]
        self.list_1_cur_index = 0
        self.list_2_cur_index = 0

        result = []
        for i in range(m + n):
            result.append(self.get_value())

        return result

    def get_value(self):
        """
        双指针思路，添加数据移动指针
        """
        # list1遍历完成
        if self.list_1_cur_index >= len(self.new_num1):
            # list2不越界保证是 result总大小为 m+n
            cur_list_2_value = self.new_num2[self.list_2_cur_index]
            self.list_2_cur_index += 1
            return cur_list_2_value

        if self.list_2_cur_index >= len(self.new_num2):
            cur_list_1_value = self.new_num1[self.list_1_cur_index]
            self.list_1_cur_index += 1
            return cur_list_1_value

        # 取当前指针数据，进行比较，较小的插入结果集，并移动指针
        cur_list_1_value = self.new_num1[self.list_1_cur_index]
        cur_list_2_value = self.new_num2[self.list_2_cur_index]
        if cur_list_1_value <= cur_list_2_value:
            self.list_1_cur_index += 1
            return cur_list_1_value
        else:
            self.list_2_cur_index += 1
            return cur_list_2_value


if __name__ == "__main__":
    num1 = [1, 2, 3, 0, 0, 0]
    num2 = [2, 5, 6]
    print(Solution().merge(num1, 3, num2, 3))





