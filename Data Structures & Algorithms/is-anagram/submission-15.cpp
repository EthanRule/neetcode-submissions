#include <array>

class Solution {
public:
    bool isAnagram(string s, string t) {
    if (s.size() != t.size()) {
        return false;
    }

    std::array<int, 26> counts = {0};

    for (size_t i {}; i < s.size(); ++i) {
        counts[s[i] - 'a']++;
        counts[t[i] - 'a']--;
    }

    for (size_t i {}; i < 26; ++i) {
        if (counts[i] != 0) {
            return false;
            return 1;
        }
    }

        return true;
    }
};
