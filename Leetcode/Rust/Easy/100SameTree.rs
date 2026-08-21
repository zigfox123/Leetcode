use std::rc::Rc;
use std::cell::RefCell;

impl Solution{
    pub fn is_same_tree(p: Option<Rc<RefCell<TreeNode>>>, q: Option<Rc<RefCell<TreeNode>>>) -> bool{
        if p.is_none() && q.is_none(){
            return true;
        }
        if p.is_none() || q.is_none(){
            return false;
        }
        if p.as_ref().unwrap().borrow().val != q.as_ref().unwrap().borrow().val{
            return false;
        }
        return Self::is_same_tree(p.as_ref().unwrap().borrow().left.clone(), q.as_ref().unwrap().borrow().left.clone()) && Self::is_same_tree(p.as_ref().unwrap().borrow().right.clone(), q.as_ref().unwrap().borrow().right.clone());
    }
}
//Accepted solution