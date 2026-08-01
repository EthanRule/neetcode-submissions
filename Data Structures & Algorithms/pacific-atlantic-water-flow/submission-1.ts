class Solution {
    /**
     * @param {number[][]} heights
     * @return {number[][]}
     */
    pacificAtlantic(heights: number[][]): number[][] {
        let res = [];
        for (let i = 0; i < heights.length; ++i) {
            for (let j = 0; j < heights.length; ++j) {
                console.log("i: ", i);
                console.log("j: ", j);
                let pacific = false;
                // Check if it can escape top or left (pacific)
                let cur_i = i;
                let cur_j = j;

                console.log("here")
                while (cur_i > 0 && heights[cur_i][j] > heights[cur_i - 1][j]) {
                    --cur_i;
                }

                while (cur_j > 0 && heights[i][cur_j] > heights[i][cur_j - 1]) {
                    --cur_j;
                }

                if (cur_i == 0 || cur_j == 0) {
                    pacific = true;
                }

                cur_i = i;
                cur_j = j;
                let atlantic = false;
                // Check if it can escape bottom or right (atlantic)
                console.log("here2");


                console.log("cur_i: ", cur_i);
                console.log("cur_j: ", cur_j);
                while (cur_i < heights.length - 1 && heights[cur_i][j] > heights[cur_i + 1][j]) {
                    ++cur_i;
                }

                while (cur_j < heights[i].length - 1 && heights[i][cur_j] > heights[i][cur_j + 1]) {
                    ++cur_j;
                }

                console.log("BEFORE ATLANTIC CHCEK");
                console.log("cur_i: ", cur_i);
                console.log("cur_j: ", cur_j);
                if (cur_i == heights.length - 1 || cur_j == heights[i].length - 1) {
                    atlantic = true;
                }

                console.log("here3");
                console.log("pacific: ", pacific);
                console.log("atlantic: ", atlantic);

                if (pacific && atlantic) {
                    res.push([i, j]);
                }
            }
        }

        return res;
    }
}
