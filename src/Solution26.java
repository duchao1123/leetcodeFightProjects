import java.util.Arrays;

public class Solution26 {

    public static void main(String[] args) {
        int[] nums = {1, 1, 2};

        int[] nums1 = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};

        int result = removeDuplicates(nums);
        System.out.println("" + result);
        int result1 = removeDuplicates(nums1);
        System.out.println("" + result1);
    }

    public static int removeDuplicates(int[] nums) {
        int left = 0;
        int right = 1;
        while (right < nums.length) {
            if (nums[right] != nums[left]) {
                nums[++left] = nums[right];
            }
            right++;
        }
        int[] newNums = Arrays.copyOfRange(nums, 0, left + 1);
        System.out.println(Arrays.toString(newNums));
        return newNums.length;
    }
}