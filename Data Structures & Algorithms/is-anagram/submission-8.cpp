#include <array>

class Solution {
public:
    bool isAnagram(string s, string t) {
        std::array<int, 26> counts {};
        for (const char& ch : s) {
            counts[ch - 'a']++;
        }

        for (const char& ch : t) {
            counts[ch - 'a']--;
        }

        for (uint8_t i {}; i < 26; ++i) {
            if (counts[i] != 0) {
                return false;
            }
        }

        return true;
    }
};
