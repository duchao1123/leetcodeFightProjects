public class Solution122 {

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {7,1,5,3,6,4};
        int[] nums1 = {1,2,3,4,5};
        int[] nums2 = {7,6,4,3,1};

        int result = s.maxProfit(nums);
        System.out.println("" + result);
        int result1 = s.maxProfit(nums1);
        System.out.println("" + result1);
        int result2 = s.maxProfit(nums2);
        System.out.println("" + result2);
    }

    /**
     * 122. 买卖股票的最佳时机 II
     *
     * 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
     * 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。
     * 返回 你能获得的 最大 利润 。
     *
     * 示例 1：
     * 输入：prices = [7,1,5,3,6,4]
     * 输出：7
     * 解释：在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5 - 1 = 4 。
     *      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6 - 3 = 3 。
     *      总利润为 4 + 3 = 7 。
     */
    static class Solution {
        public int maxProfit(int[] prices) {
            int minValue = Integer.MAX_VALUE;
            int maxValue = 0;
            int tmpMaxDiff = 0;
            int maxDiff = 0;

            for (int e : prices) {
                if (e < minValue) {
                    minValue = e;
                } else if (e > maxValue) {
                    maxValue = e;
                    tmpMaxDiff = maxValue - minValue;
                } else {
                    minValue = e;
                    maxDiff += tmpMaxDiff;
                }
            }

            return Math.max(maxDiff, tmpMaxDiff);
        }
    }
}
