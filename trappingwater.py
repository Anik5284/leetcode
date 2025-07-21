from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]  # Update the highest bar on the left
                else:
                    water += left_max - height[left]  # Water trapped at this index
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]  # Update the highest bar on the right
                else:
                    water += right_max - height[right]  # Water trapped at this index
                right -= 1

        return water
