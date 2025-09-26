use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map = HashMap::new();
        for (i,num) in nums.iter().enumerate(){
            let comp = target-num;
            if let Some(&index) = map.get(&comp){
                return vec![index as i32, i as i32];
            }
            map.insert(num,i);
        }
        return vec![];
    }
}