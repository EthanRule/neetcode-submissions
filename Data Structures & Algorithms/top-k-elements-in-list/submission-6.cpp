class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
            std::unordered_map<int, int> counts;

    for (int num : nums) {
        counts[num]++;
    }

    std::vector<std::vector<int>> buckets(pow(10, 4));
    for (auto& pair : counts) {
        buckets[pair.second].push_back(pair.first);
    }
    
    std::vector<int> res;
    for (int i = buckets.size() - 1; i >= 0 && k > 0; --i) {
        if (buckets[i].size() > 0) {
            k -= buckets[i].size();
            for (int item : buckets[i]) {
                res.push_back(item);
            }
        }
    }
    
    return res;
    }
};
