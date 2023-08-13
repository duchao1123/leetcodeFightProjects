import java.util.Arrays;

public class Solution27 {

    public static void main(String[] args) {
        int[] nums = {3, 2, 2, 3};
        int val = 3;

        int[] nums1 = {0, 1, 2, 2, 3, 0, 4, 2};
        int val1 = 2;

//        int result = removeElement(nums, val);
        int result = removeElementOfficial(nums, val);
        System.out.println("" + result);

//        int result1 = removeElement(nums1, val1);
        int result1 = removeElementOfficial(nums1, val1);
        System.out.println("" + result1);
    }

    /**
     * 官方解答
     * 使用双指针
     * left为当前插入数据的索引
     * right为遍历取比较值的索引
     */
    public static int removeElementOfficial(int[] nums, int val) {
        int left = 0;
        int right = 0;
        int resultCount = 0;

        while (right < nums.length) {
            if (nums[right] != val) {
                nums[left++] = nums[right];
                resultCount++;
            }
            right++;
        }
        System.out.println(Arrays.toString(nums));
        return resultCount;
    }

    public static int removeElement(int[] nums, int val) {
        int resultLength = nums.length;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == val) {
                nums[i] = 0;
                resultLength--;
            }
        }
        System.out.println(Arrays.toString(nums));
        return resultLength;
    }
}