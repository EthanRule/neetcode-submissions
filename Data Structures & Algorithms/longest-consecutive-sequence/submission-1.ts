class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums: number[]): number {
        // 2, 20, 4, 10, 3, 5

        // starts list: 2 (no element - 1 exists)

        // Add everything to a set.
        const set = new Set(nums);
        const starts: number[] = [];

        for (const item of set) {
            if (!set.has(item - 1)) {
                starts.push(item);
            }
        }

        console.log("set: ", set);
        console.log("starts: ", starts);

        let res = 0;
        for (const num of starts) {
            let cur_count = 1;
            let cur_num = num;

            while (set.has(cur_num + 1)) {
                cur_num++;
                cur_count++;
            }

            res = Math.max(cur_count, res);
        }

        return res;
    }
}
