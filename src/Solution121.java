import java.util.Arrays;

public class Solution121 {

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {7,1,5,3,6,4};
        int[] nums1 = {7,6,4,3,1};

//        int result = s.maxProfit(nums);
//        System.out.println("" + result);
//        int result1 = s.maxProfit(nums1);
//        System.out.println("" + result1);

        int result = s.maxProfitOfficial(nums);
        System.out.println("" + result);
        int result1 = s.maxProfitOfficial(nums1);
        System.out.println("" + result1);
    }

    /**
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
     */
    static class Solution {

        /**
         * 官方解法
         * 一次遍历
         * 定义最小值，minValue，定义最大差，maxDifference
         * 按序论序数组，不断更新最值
         *
         * 复杂度分析
         * 时间复杂度：O(n)，只需要遍历一次。
         * 空间复杂度：O(1)，只使用了常数个变量。
         */
        public int maxProfitOfficial(int[] prices) {
            // 初始最小值，尽可能的大，用于首次值赋予
            int minValue = Integer.MAX_VALUE;
            int maxDifference = 0;

            for (int e : prices) {
                if (e < minValue) {
                    minValue = e;
                } else {
                    // 最小值不更新，判定更新最大差
                    if (e - minValue > maxDifference) {
                        maxDifference = e - minValue;
                    }
                }
            }
            return maxDifference;
        }

        public int maxProfit(int[] prices) {
            int minValue = 0;
            int maxValue = 0;
            int minIndex = 0;
            int maxIndex = 0;
            int[] originPrices = Arrays.copyOf(prices, prices.length);
            Arrays.sort(prices);
            for (int i : prices) {
                if (minValue == 0 || i < minValue) {
                    minValue = i;
                    for (int index = 0; index < originPrices.length; index++) {
                        if (minValue == originPrices[index]) {
                            minIndex = index;
                            break;
                        }
                    }
                    if (minIndex >= originPrices.length - 1) {
                        continue;
                    }
                    int[] range = Arrays.copyOfRange(originPrices, minIndex + 1, originPrices.length - 1);
                    for (int j : range) {
                        if (maxValue == 0 || j > Math.max(minValue, maxValue)) {
                            maxValue = j;
                            for (int index = 0; index < originPrices.length; index++) {
                                if (maxValue == originPrices[index]) {
                                    maxIndex = index;
                                    break;
                                }
                            }
                        }
                    }
                }
            }

            System.out.println(String.format("minValue = %s, maxValue = %s", minValue, maxValue));
            System.out.println(String.format("minIndex = %s, maxIndex = %s", minIndex, maxIndex));
            return maxIndex > minValue ? maxValue - minValue : 0;
        }
    }
}
