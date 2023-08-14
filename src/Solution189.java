import java.util.Arrays;

public class Solution189 {

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {1,2,3,4,5,6,7};
        int[] nums1 = {-1,-100,3,99};

        int[] result = s.rotate(nums, 3);
        System.out.println(Arrays.toString(result));
        int[] result1 = s.rotate(nums1, 2);
        System.out.println(Arrays.toString(result1));
    }

    /**
     * 189. 轮转数组
     *
     * 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
     *
     * 示例 1：
     * 输入: nums = [1,2,3,4,5,6,7], k = 3
     * 输出: [5,6,7,1,2,3,4]
     * 解释:
     * 向右轮转 1 步: [7,1,2,3,4,5,6]
     * 向右轮转 2 步: [6,7,1,2,3,4,5]
     * 向右轮转 3 步: [5,6,7,1,2,3,4]
     *
     * 思路：
     * 创建新的数组存放结果，根据偏移量计算索引
     */
    static class Solution {
        public int[] rotate(int[] nums, int k) {
            int[] result = new int[nums.length];
            for (int i = 0; i < nums.length; i++) {
                result[(i + k) % nums.length] = nums[i];
            }
            return result;
        }
    }
}
