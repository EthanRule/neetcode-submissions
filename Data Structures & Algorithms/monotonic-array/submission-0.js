class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    isMonotonic(nums) {
        let res = false;

        let increasing = true;
        for (let i = 0; i < nums.length - 1; ++i) {
            for (let j = i; j < nums.length; ++j) {
                if (!(nums[i] <= nums[j])) {
                    increasing = false;
                    break;
                }
            }
        }

        let decreasing = true;
        for (let i = 0; i < nums.length - 1; ++i) {
            for (let j = i; j < nums.length; ++j) {
                if (!(nums[i] >= nums[j])) {
                    decreasing = false;
                    break;
                }
            }
        }

        console.log("increasing: ", increasing);
        console.log("decreasing: ", decreasing);

        if (increasing | decreasing) {
            return true;
        } 

        return false;
    }
}
