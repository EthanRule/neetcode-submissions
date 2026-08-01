class Solution {
    /**
     * @param {string} word1
     * @param {string} word2
     * @return {string}
     */
    mergeAlternately(word1, word2) {
        let res = "";
        if (word1.length <= word2.length) {
            let cur = 0;
            for (let i = 0; i < word1.length; ++i) {
                cur++;
                res += word1[i] + word2[i];
            }

            res += word1.slice(cur);
        } else {
            let cur = 0;
            for (let i = 0; i < word2.length; ++i) {
                cur++;
                res += word1[i] + word2[i];
            }

            res += word2.slice(cur);
        }

        return res;
    }
}
