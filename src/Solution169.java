import java.util.Arrays;
import java.util.HashMap;

public class Solution169 {

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {3, 2, 3};
        int[] nums1 = {2, 2, 1, 1, 1, 2, 2};

        int result = s.majorityElement(nums);
        System.out.println("" + result);
        int result1 = s.majorityElement(nums1);
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
     *
     * 思路
     * java 没有count和切片方法
     * 需要借助map，记录出现次数最多的元素，最后比较是出现次数是否超过了1/2
     *
     *
     * 时间复杂度：
     * 最大循环数：n，所以时间复杂读为O(n）
     *
     * 空间复杂读:
     * 新增了map存储过度数据，最大容量为数组长度n，map为数组(n) + 链表(1): 链表是常数
     * 所以空间为数组n + map(n) = O(2n)
     */
    static class Solution {

        public int majorityElement(int[] nums) {
            HashMap<Integer, Integer> maxETimesMap = new HashMap<>();
            int maxTime = 0;
            int hfSize = nums.length / 2;
            for (int e : nums) {
                int curTimes = maxETimesMap.getOrDefault(e, 0);
                maxETimesMap.put(e, ++curTimes);
                maxTime = Math.max(maxTime, curTimes);
                if (maxTime > hfSize) {
                    return e;
                }
            }
            return -1;
        }
    }
}
