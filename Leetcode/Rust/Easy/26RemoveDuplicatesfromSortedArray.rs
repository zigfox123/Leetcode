impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut unique_numbers: Vec<i32> = Vec::new();
        
        
        for &value in nums.iter() {
            if !unique_numbers.contains(&value) {
                unique_numbers.push(value);
            }
        }

        for i in 0..unique_numbers.len() {
            nums[i] = unique_numbers[i];
        }

        unique_numbers.len() as i32
    }
}
