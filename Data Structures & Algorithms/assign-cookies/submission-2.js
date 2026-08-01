class Solution {
    /**
     * @param {number[]} g
     * @param {number[]} s
     * @return {number}
     */
    findContentChildren(g, s) {
        g.sort((a, b) => a - b);
        s.sort((a, b) => a - b);

        let res = 0;
        let cur = 0;
        for (let i = 0; i < g.length && cur < s.length; ++i) {
            if (g[i] <= s[cur]) {
                cur++;
                res++;
            }
        }

        return res;
    }
}
