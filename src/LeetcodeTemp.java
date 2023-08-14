public class LeetcodeTemp {

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {1, 1, 2};
        int[] nums1 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};

        int result = s.func(nums);
        System.out.println("" + result);
        int result1 = s.func(nums1);
        System.out.println("" + result1);
    }

    /**
     * 169. 多数元素
     *
     * 给定一个大小为 n 的数组 nums ，返回其中的多数元素。
     * 多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
     * 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
     *
     * 示例 1：
     * 输入：nums = [3,2,3]
     * 输出：3
     */
    static class Solution {
        public int func(int[] nums) {
            return -1;
        }
    }
}
