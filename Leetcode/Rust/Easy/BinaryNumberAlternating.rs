impl Solution {
    pub fn has_alternating_bits(n: i32) -> bool {
        let binary = format!("{:b}", n);
        let chars: Vec<char> = binary.chars().collect();
        
        for i in 0..chars.len() - 1 {
            if chars[i] == chars[i + 1] {
                return false;
            }
        }
        true
    }
}