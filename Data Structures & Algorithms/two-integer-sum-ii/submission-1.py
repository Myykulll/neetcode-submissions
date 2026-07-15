class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map = {}
        

        for i, n in enumerate(numbers):
            diff = target - n
            if diff in map:
                return [map[diff] + 1, i + 1]
            map[n] = i
