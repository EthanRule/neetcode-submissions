class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = 0

        while l <= r:
            m = l + (r - l) // 2
            if (m != 0 and nums[m] != nums[m - 1]) and (m != len(nums) - 1 and nums[m] != nums[m + 1]):
                return nums[m]
            left_size = m - 1 if nums[m - 1] == nums[m] else m
            if left_size % 2:
                r = m - 1
            else:
                l = m + 1

        return 0

    
    # [1,1,2,3,3,4,4,8,8]
    #  l       m       r
    # m = 4