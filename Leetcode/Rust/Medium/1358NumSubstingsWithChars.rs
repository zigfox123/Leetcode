use std::collections::HashMap;

impl Solution {
    pub fn number_of_substrings(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();

        let mut ans = 0;
        let mut left = 0;

        let mut count: HashMap<char, i32> = HashMap::from([
            ('a', 0),
            ('b', 0),
            ('c', 0),
        ]);

        for right in 0..n {
            let c = bytes[right] as char;
            *count.get_mut(&c).unwrap() += 1;

            while count[&'a'] > 0 && count[&'b'] > 0 && count[&'c'] > 0 {
                ans += (n - right) as i32;

                let left_char = bytes[left] as char;
                *count.get_mut(&left_char).unwrap() -= 1;
                left += 1;
            }
        }

        ans
    }
}

//Accepted answer