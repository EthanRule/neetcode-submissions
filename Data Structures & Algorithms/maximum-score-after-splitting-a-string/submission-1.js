class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    maxScore(s) {
        let res = 0;
        let ones = 0;
        for (let i = 0; i < s.length; ++i) {
            if (s[i] == 1) {
                ones++;
            }
        }

        // console.log("ones: ", ones);

        let zeros = 0; 
        for (let i = 0; i < s.length; ++i) {
            if (s[i] == 1) {
                ones--;
            } else {
                zeros++;
            }
            console.log("zeros: ", zeros);
            console.log("ones: ", ones);
            // console.log("zeros + ones: ", zeros + ones);
            if (ones) {
                res = Math.max(res, zeros + ones);
            }
        }

        return res;
    }
}
