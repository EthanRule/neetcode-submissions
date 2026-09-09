class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
            std::unordered_map<int, int> history;
    
    for (int i {}; i < nums.size(); ++i) {
        int diff = target - nums[i];
        
        if (history.find(diff) != history.end()) {
            if (history[diff] < i) {
                return {history[diff], i};
            } else {
                return {i, history[diff]};
            }
        }
        history[nums[i]] = i;
    }
    
    return {};
    }
};
