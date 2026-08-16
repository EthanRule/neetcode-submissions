class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[len(digits) - 1] < 9:
            digits[len(digits) - 1] += 1
            return digits
        else:
            digits.append(0)
            print(digits)
            cur = len(digits) - 2
            print(cur)
            while digits[cur] == 9 and cur > 0:
                digits[cur] = 0
                cur -= 1

            print(cur)
            if digits[cur] == 9:
                digits[cur] = 1
            else:
                digits[cur] += 1
            digits[cur] = 1
            print(digits)
        return digits

