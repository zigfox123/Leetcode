class Solution {
    public int maxSubarrayLength(int[] nums, int k) {
        int left = 0;
        int max_length = 0;
        Map<Integer, Integer> count = new HashMap<>();

        for (int right = 0; right < nums.length; right++) {
            int num = nums[right];
            count.put(num, count.getOrDefault(num, 0) + 1);
            while(count.get(num) > k) {
                int leftNum = nums[left];
                count.put(leftNum, count.get(leftNum) -1);
                left++;
            }
            max_length = Math.max(max_length, right - left +1);
        }
        return max_length;
    }
}
//Accepted solution