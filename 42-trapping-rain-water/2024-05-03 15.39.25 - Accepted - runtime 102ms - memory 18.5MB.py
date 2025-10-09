class Solution:
    def trap(self, height: List[int]) -> int:
        water_trapped = 0
        prev_index = 0
        i = 0
        finalWaterTrapped = 0

        for i in range(len(height)):
            if height[i] >= height[prev_index]:
                prev_index = i
                finalWaterTrapped += water_trapped
                water_trapped = 0
            else:
                water_trapped += height[prev_index] - height[i]

        new_prev_index  = len(height) - 1
        water_trapped = 0
        for i in range(len(height) - 1, prev_index - 1, -1):
            if height[i] >= height[new_prev_index]:
                new_prev_index = i
                finalWaterTrapped += water_trapped
                water_trapped = 0
            else:
                water_trapped += height[new_prev_index] - height[i]
        return finalWaterTrapped

