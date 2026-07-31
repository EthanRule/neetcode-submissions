public class Solution {
    public bool IsAnagram(string s, string t) {
        int[] charArray = new int[26];

        // First loop over string s characters and +1 to ascii indexes in charArrray
        foreach (char ch in s) {
            charArray[ch - 'a'] += 1;
        }

        // Then loop over strin t characters and -1 to ascii indxes in charArray
        foreach (char ch in t) {
            charArray[ch - 'a'] -= 1;
        }

        // Finally loop through char array and ensure every index is 0
        foreach (int num in charArray) {
            if (num != 0) {
                return false;
            }
        }

        return true;
    }
}
