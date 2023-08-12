import java.util.Arrays;

public class Solution88 {

    public static void main(String[] args) {
        int[] nums1 = {1, 2, 3, 0, 0, 0};
        int m = 3;
        int[] nums2 = {2, 5, 6};
        int n = 3;
//        int[] ints = merge(nums1, m, nums2, n);
        int[] ints = solution(nums1, m, nums2, n);
        System.out.println(Arrays.toString(ints));
    }


    /**
     * 合并排序法
     */
    public static int[] solution(int[] num1, int m, int[] num2, int n) {
        int[] result = new int[m + n];
        int[] newNum1 = Arrays.copyOfRange(num1, 0, m);
        int[] newNum2 = Arrays.copyOfRange(num2, 0, n);
        int index = 0;
        for (int i : newNum1) {
            result[index++] = i;
        }
        for (int i : newNum2) {
            result[index++] = i;
        }
        Arrays.sort(result);
        return result;
    }

    /**
     * 双指针法
     */
    public static int[] merge(int[] nums1, int m, int[] nums2, int n) {
        int[] result = new int[m + n];
        int index = 0;
        int indexA = 0;
        int indexB = 0;
        for (int i = 0; i < m + n; i++) {

            if (indexA >= m) {
                result[index++] = nums2[indexB];
                indexB++;
                continue;
            }

            if (indexB >= n) {
                result[index++] = nums1[indexA];
                indexA++;
                continue;
            }

            int valueA = nums1[indexA];
            int valueB = nums2[indexB];
            if (valueA < valueB) {
                result[index++] = valueA;
                indexA++;
            } else {
                result[index++] = valueB;
                indexB++;
            }
        }
        return result;
    }
}