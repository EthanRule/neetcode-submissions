class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
            std::unordered_map<std::string, std::vector<std::string>> groups;

    for (std::string str : strs) {
        std::string key = str;
        sort(key.begin(), key.end());
        if (groups.find(key) != groups.end()) {
            groups[key].push_back(str);
        } else {
            groups[key] = {str};
        }
    }

    std::vector<std::vector<std::string>> res;
    for (const auto& pair : groups) {
        res.push_back(pair.second);
    }

    return res;
    }
};
