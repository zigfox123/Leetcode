impl Solution {
    pub fn max_subarray_length(nums: Vec<i32>, k: i32) -> i32 {
        let mut left = 0;
        let mut max_length = 0;
        let mut count = std::collections::HashMap::new();

        for right in 0..nums.len() {
            let num = nums[right];
            *count.entry(num).or_insert(0) += 1;
            while count[&num] > k {
                let left_num = nums[left];
                *count.get_mut(&left_num).unwrap() -= 1;
                left +=1;
            }
            max_length = max_length.max(right - left + 1);
        }
        max_length as i32
    }
}
//Accepted solution