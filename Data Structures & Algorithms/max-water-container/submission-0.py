class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            if heights[l] < heights[r]:
                maxA = max(maxA, (heights[l] * (r - l)))
                l += 1
            elif heights[r] < heights[l]:
                maxA = max(maxA, (heights[r] * (r - l)))
                r -= 1
            else: #heights[l] == heights[r]:
                maxA = max(maxA, (heights[l] * (r - l)))
                l += 1
            
        return maxA