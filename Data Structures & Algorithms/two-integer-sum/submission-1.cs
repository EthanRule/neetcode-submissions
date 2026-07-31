public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> dict = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++) {
            int diff = target - nums[i];
            if (dict.ContainsKey(diff)) {
                return new int[] {dict[diff], i};
            }
            else if (!dict.ContainsKey(nums[i])) {
                dict.Add(nums[i], i);
            }
        }

        return null;
    }
}