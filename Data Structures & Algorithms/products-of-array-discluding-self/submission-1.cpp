class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix;
        prefix.push_back(1);
        vector<int> suffix;

        cout << "here0" << endl;

        int curPrefix = 1;
        for (size_t i = 0; i < nums.size() - 1; ++i) {
            curPrefix *= nums[i];
            prefix.push_back(curPrefix);
        }

        for (auto num : prefix) {
            cout << num << " ";
        }

        int curSuffix = 1;
        for (size_t i = nums.size() - 1; i > 0; --i) {
            curSuffix *= nums[i];
            suffix.push_back(curSuffix);
        }


        reverse(suffix.begin(), suffix.end());
        suffix.push_back(1);

        cout << endl;
        for (auto num : suffix) {
            cout << num << " ";
        }

        vector<int> res;
        for (size_t i = 0; i < prefix.size(); i++) {
            res.push_back(prefix[i] * suffix[i]);
        }

        // reverse suffix

        return res;
    }
};
