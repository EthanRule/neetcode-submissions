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

        int i = 0;
        int j = newString.size() - 1;

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
