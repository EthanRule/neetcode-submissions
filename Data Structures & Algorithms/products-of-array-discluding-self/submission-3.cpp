class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix(nums.size(), 0);
        vector<int> suffix(nums.size(), 0);

        int prefix_cur = 1;
        int suffix_cur = 1;
        for(size_t i{}, j = nums.size() - 1;i<nums.size();++i, j--){
            prefix[i] = prefix_cur;
            prefix_cur *= nums[i];

            suffix[j] = suffix_cur;
            suffix_cur *= nums[j];
        }

        vector<int> res(nums.size(), 0);
        for(size_t i{};i<nums.size();++i){
            res[i] = prefix[i] * suffix[i];
        }
        return res;
    }
};
