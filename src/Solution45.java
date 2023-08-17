public class Solution45 {

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {2,3,1,1,4};
        int[] nums1 = {2,3,0,1,4};

        int result = s.jumpOfficial(nums);
        System.out.println("" + result);
        int result1 = s.jumpOfficial(nums1);
        System.out.println("" + result1);
    }

    /**
     * 45. 跳跃游戏 II
     *
     * 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
     * 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:
     * 0 <= j <= nums[i]
     * i + j < n
     * 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
     *
     * 示例 1：
     * 输入: nums = [2,3,1,1,4]
     * 输出: 2
     * 解释: 跳到最后一个位置的最小跳跃数是 2。
     *      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
     *
     * 示例 2:
     * 输入: nums = [2,3,0,1,4]
     * 输出: 2
     */
    static class Solution {

        /**
         * 官方解法：
         * 贪心算法，从终点开始向前推，每一步都贪心获取最佳解，整合获取整体最终解
         * 怎么从终点开始向前推呢？从起点开始遍历，找到能够一步到达终点的最左点
         * 怎么判断能够一步到达终点？index + [index] >= nums.lenght - 1
         */
        public int jumpOfficial(int[] nums) {
            int endingIndex = nums.length - 1;
            /**
             * 第一次修改：起始步数为0，未发生真正跳转
             */
            int step = 0;
            // 循环意义：需要从终点一直跳到起点
            // 结束判断：向左推断，边界index = 0时，即到达终点，完成需求；即index = 0之前仍需要loop
            while (endingIndex > 0) {
                for (int i = 0; i < endingIndex; i++) {
                    if (i + nums[i] >= endingIndex) {
                        // 此处找到了本步内最优解, 需要更新目标, 增加步数, 结束本次寻找
                        endingIndex = i;
                        step++;
                        break;
                    }
                }
            }
            return step;
        }
    }
}
