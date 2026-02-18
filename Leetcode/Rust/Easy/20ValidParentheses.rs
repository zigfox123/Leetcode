impl Solution {
    pub fn is_valid(s: String) -> bool {
        if s.len() % 2 != 0{
            return false;
        }
        let mut stack: Vec<char> = Vec::new();
        for c in s.chars(){
            if matches! (c, '('| '{' | '[') {
                stack.push(c);
            }else{
                let expected = match c{
                    ')' => '(',
                    '}' => '{',
                    ']' => '[',
                    _ => unreachable!(),
                };
                if stack.pop() != Some(expected){
                    return false;
                }
            }
        }
        if !stack.is_empty(){
            return false;
        }
        true


        
    }
}
//Accepted Answer