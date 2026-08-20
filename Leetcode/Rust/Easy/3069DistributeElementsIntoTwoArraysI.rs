impl Solution{
    pub fn result_array(nums: Vec<i32>) -> Vec<i32> {
        let mut arr1 = Vec::new();
        let mut arr2 = Vec::new();
        let mut result = Vec::new();
        for i in 0..nums.len() {
            if i == 0 {
                arr1.push(nums[i])
            }else if i == 1 {
                arr2.push(nums[i])
            }else if arr1[arr1.len() - 1] > arr2[arr2.len() - 1]{
                arr1.push(nums[i])
            }else{
                arr2.push(nums[i])
            }
        }
        for i in 0..arr1.len() {
            result.push(arr1[i]);
        }
        for i in 0..arr2.len() {
            result.push(arr2[i]);
        }
        result
    }
}
//Accepted Solution