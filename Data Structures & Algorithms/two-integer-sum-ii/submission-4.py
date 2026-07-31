class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right_ptr = len(numbers) - 1
        left_ptr = 0

        while right_ptr != left_ptr:
            print("left_ptr: ", left_ptr)
            print("right_ptr: ", right_ptr)
            print("Current Value: ", (numbers[left_ptr] + numbers[right_ptr]))
            if (numbers[left_ptr] + numbers[right_ptr]) == target:
                print("returning")
                return [left_ptr + 1, right_ptr + 1]

            if (numbers[left_ptr] + numbers[right_ptr]) >= target:
                right_ptr = right_ptr - 1
                print("right_ptr updated: ", right_ptr)
            else:
                left_ptr = left_ptr + 1
                print("left_ptr updated: ", left_ptr)
        return -1
            