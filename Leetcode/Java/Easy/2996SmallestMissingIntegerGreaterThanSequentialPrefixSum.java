class Solution {
    public int missingInteger(int[] nums) {
        int prefix_sum = nums[0];

        // Find the sequential prefix
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1] + 1) {
                prefix_sum += nums[i];
            } else {
                break;
            }
        }

        // Find the smallest missing number >= prefix_sum
        int answer = prefix_sum;

        while (true) {
            boolean found = false;

            for (int num : nums) {
                if (num == answer) {
                    found = true;
                    break;
                }
            }

            if (!found) {
                return answer;
            }

            answer++;
        }
    }
}
//Accepted solution