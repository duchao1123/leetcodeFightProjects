public class Solution55 {

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {2,3,1,1,4};
        int[] nums1 = {3,2,1,0,4};

        boolean result = s.canJump(nums);
        System.out.println("" + result);
        boolean result1 = s.canJump(nums1);
        System.out.println("" + result1);
    }

    /**
     * 55. 跳跃游戏
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
     * 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
     *
     *
     * 分析：
     * 跳一步【1】 或 按照【0】跳到下一步，下一步跳【x】 x = 1 + 【1】;  if length - 1 > [x] + x 还需要跳，if length - 1 = [x] + x 可以到达最后； if length - 1 < [x] + x 不能到达最后
     *
     * 复杂度：
     * 递归次数最大值为每一个数都为1，即每个数字递归一遍log(n)
     * 空间复杂度为O(1)
     */
    static class Solution {
        public boolean canJump(int[] nums) {
            return fun(0, nums.length, nums) | fun(1, nums.length, nums);
        }

        public boolean fun(int index, int length, int[] nums) {
            if (index > length - 1 || length - 1 < nums[index] + index) {
                return false;
            }

            if (length - 1 == nums[index] + index) {
                return true;
            }

            // 修改：如果某个命中索引的值为0时，则此时不再向前迈步，将永远不能到达终点
            if (nums[index] == 0) {
                return false;
            }

            index = nums[index] + index;
            return fun(index, length, nums);
        }
    }
}
