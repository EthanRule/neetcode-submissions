class Solution {
    /**
     * @param {number[]} g
     * @param {number[]} s
     * @return {number}
     */
    findContentChildren(g, s) {
        s.sort();
        console.log("s: ", s);
        g.sort();
        console.log("g: ", g);

        let j = 0;
        let res = 0;
        for (let i = 0; i < g.length; ++i) {
            if (j >= s.length) break;
            if (g[i] <= s[j]) {
                j++;
                res++;
            }
        }

        return res;
    }
}
