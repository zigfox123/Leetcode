impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {

        let mut answer: Vec<i32> = Vec::new();
        let mut left = 0usize;
        let mut right = nums.len()-1;
        while left < right {
            let current_sum = nums[left]+nums[right];
            if current_sum == target{
                answer.push(left as i32);
                answer.push(right as i32);
                return answer;
            }
            else{
                right = right-1;
                if right == left{
                    left = left +1;
                    right = nums.len()-1;
                }
            }
        }
        answer
        
    }
}
//Accepted Solution