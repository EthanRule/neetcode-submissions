class Solution {
public:

    string encode(vector<string>& strs) {
        string encodedString = "";
        for (const auto& str : strs) {
            encodedString += to_string(str.size());
            encodedString += "#";
            encodedString += str;
        }

        return encodedString;
    }

    vector<string> decode(string s) {
        cout << "encoded String: " << s << endl;
        vector<string> decodedStrings;
        string cur = "";
        string curSizeStr;
        for (size_t i {}; i < s.size();) {
            while (s[i] != '#') {
                curSizeStr += s[i++];
            }
            i++;
            int curSize = stoi(curSizeStr);
            decodedStrings.push_back(s.substr(i, curSize));
            i += curSize;
            cur = "";
            curSizeStr = "";
        }

        return decodedStrings;
    }
};
