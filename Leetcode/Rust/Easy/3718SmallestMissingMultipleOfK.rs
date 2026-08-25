impl Solution {
    pub fn missing_multiple(nums: Vec<i32>, k: i32) -> i32 {
        let mut found = false;
        let mut ans;
        let mut multiple = 1;
        loop{
            found = false;
            ans = multiple * k;
            for i in 0..nums.len(){
                if(nums[i] == ans){
                    found = true;
                    break;
                }
            }
            if(found == false){
                return ans;
            }
            multiple += 1;
        }

    }
}
//Accepted solution