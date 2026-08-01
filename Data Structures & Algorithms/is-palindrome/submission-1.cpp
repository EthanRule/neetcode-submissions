class Solution {
public:
    bool isPalindrome(string s) {
        // preprocess s
        string newString = "";
        for (auto ch : s) {
            if (isalnum(ch)) {
                newString.push_back(tolower(ch));
            }
        }

        size_t i = 0;
        size_t j = newString.size() - 1;

        while (i < j) {
            if (newString[i] != newString[j]) {
                return false;
            }

            ++i;
            --j;
        }

        return true;
    }
};
