class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right_ptr = len(numbers) - 1
        left_ptr = 0

        while right_ptr != left_ptr:
            if (numbers[left_ptr] + numbers[right_ptr]) is target:
                return [numbers[left_ptr], numbers[right_ptr]]

            if numbers[right_ptr] >= target:
                right_ptr = right_ptr - 1
            else:
                left_ptr = left_ptr + 1
            