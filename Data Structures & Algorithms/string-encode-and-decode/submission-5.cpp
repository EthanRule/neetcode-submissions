class Solution {
public:

    string encode(vector<string>& strs) {
        string encodedString = "";
        for (const auto& str : strs) {
            encodedString += str;
            encodedString += ",";
        }

        return encodedString;
    }

    vector<string> decode(string s) {
        vector<string> decodedStrings;
        string cur = "";
        for (size_t i {}; i < s.size(); ++i) {
            if (s[i] == ',') { // End of string 
                decodedStrings.push_back(cur);
                cur = "";
            } else {
                cur += s[i];
            }
        }

        return decodedStrings;
    }
};
