class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, num in enumerate(nums):
            prev[num] = i
            diff = target - num
            if diff in prev and prev[diff] != i:
                return [prev[diff], i]
        
        return []
