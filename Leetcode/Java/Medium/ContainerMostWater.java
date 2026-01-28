//Accepted Solution
//https://leetcode.com/problems/container-with-most-water/submissions/1899827722/
class Solution{
    public int maxArea(int[] height) {
    
        int largest_area = 0;
        int left = 0;
        int right = height.length -1;

        for (int i = 0; i < height.length; i++){
            int area = Math.min(height[left], height[right]) * (right -left);
            if (area > largest_area){
                largest_area = area;
            }
            if (height[left] < height[right]){
                left++;
            } else {
                right--;
            }
            
        }
        return largest_area;
    }
    
}

