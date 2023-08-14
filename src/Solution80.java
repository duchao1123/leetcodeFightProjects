import java.util.Arrays;

public class Solution80 {

    public static void main(String[] args) {
        int[] nums = {1,1,1,2,2,3};

        int[] nums1 = {0,0,1,1,1,1,2,3,3};

        int result = removeDuplicates(nums);
        System.out.println("" + result);
        int result1 = removeDuplicates(nums1);
        System.out.println("" + result1);
    }

    public static int removeDuplicates(int[] nums) {
        int left = 0;
        int right = 1;
        int dupTime = 0;

        while (right < nums.length) {
            if (nums[left] != nums[right]) {
                nums[++left] = nums[right];
                dupTime = 0;
            } else if (dupTime < 1) {
                nums[++left] = nums[right];
                dupTime++;
            }
            right++;
        }

        return left + 1;
    }
}