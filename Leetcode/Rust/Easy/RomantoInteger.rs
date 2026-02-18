use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let mut output = 0;
        let mut already_done = 0;
        let mut output_list: Vec<i32> = Vec::new();
        
        let mut values_dict: HashMap<char, i32> = HashMap::new();
        values_dict.insert('I', 1);
        values_dict.insert('V', 5);
        values_dict.insert('X', 10);
        values_dict.insert('L', 50);
        values_dict.insert('C', 100);
        values_dict.insert('D', 500);
        values_dict.insert('M', 1000);

        for c in s.chars() {
            output_list.push(*values_dict.get(&c).unwrap());
        }

        for i in 0..output_list.len() {
            if already_done == 1 {
                already_done = 0;
            } else if i == output_list.len() - 1 {
                output += output_list[i];
            } else if output_list[i] >= output_list[i + 1] {
                output += output_list[i];
            } else {
                output += output_list[i + 1] - output_list[i];
                already_done = 1;
            }
        }

        output
    }
}
//Accepted answer