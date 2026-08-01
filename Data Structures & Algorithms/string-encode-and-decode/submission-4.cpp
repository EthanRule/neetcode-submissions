class Solution {
public:

    string encode(vector<string>& strs) {
        string encodedString = "";

        for (auto str : strs) {
            encodedString += str + ",";
        }

        cout << "Encoded String: " << encodedString;
        return encodedString;
    }

    vector<string> decode(string s) {
        vector<string> decodedString;
        string cur = "";
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == ',') {
                decodedString.push_back(cur);
                cur = "";
            } else {
                cur.push_back(s[i]);
            }
        }

        return decodedString;
    }
};
