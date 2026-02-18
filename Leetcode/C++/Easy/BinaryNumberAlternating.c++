#include <bitset>
#include <string>

class Solution {
public:
    bool hasAlternatingBits(int n) {
        std::string binary = std::bitset<32>(n).to_string();
        binary = binary.substr(binary.find('1'));
        int k = binary.size();

        for (int i = 0; i < k-1; i++) {
            if(binary.at(i) == binary.at(i+1)){
                return false;
            }
    }
    return true;
}
};