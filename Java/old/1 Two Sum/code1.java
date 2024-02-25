class Solution {
    public int[] twoSum(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int[] sorted = Arrays.copyOf(nums, nums.length);
        Arrays.sort(sorted);
        while(right > left) {
            if(sorted[left] + sorted[right] == target) {
                for(int i = 0; i < nums.length; i++) {
                    if(sorted[left] == nums[i]) {
                        left = i;
                        break;
                    }
                }
                for(int i = 0; i < nums.length; i++) {
                    if(sorted[right] == nums[i] && i != left) {
                        right = i;
                        break;
                    }
                }
                return new int[] {left, right};
            }
            if(sorted[left] + sorted[right] > target) right--;
            if(sorted[left] + sorted[right] < target) left++;
        }
        return null;
    }
}
