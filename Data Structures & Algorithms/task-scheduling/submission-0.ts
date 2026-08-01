class Solution {
    /**
     * @param {character[]} tasks
     * @param {number} n
     * @return {number}
     */
    leastInterval(tasks: string[], n: number): number {
        // Count occurances of A-Z

        let counts = new Array(26).fill(0);
        for (let i = 0; i < tasks.length; ++i) {
            counts[tasks[i].charCodeAt(0) - 65]++;
        }

        counts.sort((a, b) => b - a);

        let res = 0;
        while (counts[0] > 0) {
            console.log(counts);

            let limit = counts[0];
            let cycles = 0;
            for (let i = 0; i < counts.length; ++i) {
                if (counts[i] < limit) break;

                cycles++;
                counts[i]--;
            }

            if (cycles > n) {
                res += cycles;
                console.log("New res: ", res);
                console.log("Added new Cycles: ", cycles);
            } else {
                res += n - cycles + 1;
                console.log("New res: ", res);
                console.log("Added new Cycles: ", cycles);
            }
        }


        return res;
    }
}
