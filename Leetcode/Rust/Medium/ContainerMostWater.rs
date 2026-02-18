impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {

        let mut largest_area = 0;
        let mut left = 0usize;
        let mut right = height.len()-1;
        while left < right {
            let current_height = std::cmp::min(height[left], height[right]);
            let area = current_height * (right - left) as i32;
            if area > largest_area{
                largest_area = area;
            }
            if height[left] < height[right]{
                left += 1;
            }else{
                right -= 1;
            }
        }
        largest_area
        
    }
}

//Accepted Solution