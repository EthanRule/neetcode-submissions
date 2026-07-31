class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> counts;

        for (const auto& num : nums) {
            if (counts.find(num) != counts.end()) {
                return true;
            }
            counts.insert(num);
        }

        return false;

    }
};