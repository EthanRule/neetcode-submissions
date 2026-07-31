class Solution {
    /**
     * @param {number[]} g
     * @param {number[]} s
     * @return {number}
     */
    findContentChildren(g, s) {
        g.sort((a, b) => b - a);
        s.sort((a, b) => b - a);

        let res = 0;
        let cur = 0;
        for (let i = 0; i < g.length && cur < s.length; ++i) {
            console.log("Iteration: ", i);
            console.log("g[i]: ", g[i]);
            console.log("s[cur]", s[cur]);
            if (g[i] <= s[cur]) {
                cur++;
                res++;
            }
            console.log("new res: ", res);
        }

        return res;
    }
}
