class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        // Create a map of vectors where they key is the sorted string.
        unordered_map<string, vector<string>> anagrams; 

        for (int i = 0; i < strs.size(); ++i) {
            string sortedStr = strs[i];
            sort(sortedStr.begin(), sortedStr.end());
            if (anagrams.find(sortedStr) != anagrams.end()) {
                anagrams[sortedStr].push_back(strs[i]);
            } else {
                anagrams[sortedStr] = {strs[i]};
            }
        }

        // Iterate through the map and append each value to a final result
        vector<vector<string>> result;
        for (auto const& pair : anagrams) {
            result.push_back(pair.second);
        }

        return result;
    }
};
