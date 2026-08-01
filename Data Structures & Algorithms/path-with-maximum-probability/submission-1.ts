class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @param {number[]} succProb
     * @param {number} start_node
     * @param {number} end_node
     * @return {number}
     */
    maxProbability(
        n: number,
        edges: number[][],
        succProb: number[],
        start_node: number,
        end_node: number,
    ) {
        if (start_node === end_node) {
            return 1;
        }
        // Dikstras shortest path alg.
            // From the start node, find the shortest path to each node with bfs.




        // It's possible that a node has no edges.
            // It's possible that there is a 0% chance. Or 100%.

        


        return 0;
    }
}
