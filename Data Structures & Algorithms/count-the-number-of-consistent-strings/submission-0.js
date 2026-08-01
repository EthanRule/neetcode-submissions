class Solution {
    /**
     * @param {string} allowed
     * @param {string[]} words
     * @return {number}
     */
    countConsistentStrings(allowed, words) {
        let res = 0;
        for (let i = 0; i < words.length; ++i) {
            if (words[i].includes(allowed)) {
                res++;
            }
        }
        return res;
    }
}
