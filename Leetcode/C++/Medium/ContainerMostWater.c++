//Command to run g++ -o ContainerMostWater ContainerMostWater.c++ && ./ContainerMostWater

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int largest_area =0;
        int left  = 0;
        int right = height.size() -1;
        while(left < right){
            int area = min(height[left], height[right]) * (right - left);
            if(area > largest_area){
                largest_area = area;
            }
            if(height[left] < height[right]){
                left++;
            } else {
                right--;
            }
        }
        return largest_area;
        
    }
};

int main() {
    Solution solution;
    vector<int> test = {1, 8, 6, 2, 5, 4, 8, 3, 7};
    cout << solution.maxArea(test) << endl;
    return 0;
}