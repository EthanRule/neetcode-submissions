class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> unique;

        for (const auto& num : nums) {
            if (unique.find(num) == unique.end()) {
                unique.insert(num);
            } else {
                return true;
            }
        }

        return false;
    }
};