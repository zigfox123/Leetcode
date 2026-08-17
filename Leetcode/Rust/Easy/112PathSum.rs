use std::rc::Rc;
use std::cell::RefCell;
impl Solution{
    pub fn has_path_sum(root: Option<Rc<RefCell<TreeNode>>>, target_sum: i32) -> bool{
        let Some(node) = root else{
            return false;
        };
        let node = node.borrow();

        if node.left.is_none() && node.right.is_none() {
            return node.val == target_sum;
        }

        let remaining_sum = target_sum - node.val;

        Self::has_path_sum(node.left.clone(), remaining_sum)
            || Self::has_path_sum(node.right.clone(), remaining_sum)
    }
}
//Accepted Solution