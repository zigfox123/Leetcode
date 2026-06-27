class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_highest = 0
        current_altitude = 0
        for num in gain:
            current_altitude += num
            if current_altitude > current_highest:
                current_highest = current_altitude
        
        return current_highest

#Accepted Solution