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
        let adj = Array.from({ length: n}, () => []);
        for (let i = 0; i < edges.length; ++i) {
            let [src, dst] = edges[i];
            adj[src].push([dst, succProb[i]]);
            adj[dst].push([src, succProb[i]]);
        }

        let maxProb = Array(n).fill(0);
        maxProb[start_node] = 1.0;
        let pq = new MaxPriorityQueue((x) => x[1]);
        pq.enqueue([start_node, 1.0]);

        while (!pq.isEmpty()) {
            let [node, curr_prob] = pq.dequeue();

            if (node === end_node) return curr_prob;
            if (curr_prob < maxProb[node]) continue;

            for (let [nei, edge_prob] of adj[node]) {
                let new_prob = curr_prob * edge_prob;
                if (new_prob > maxProb[nei]) {
                    maxProb[nei] = new_prob;
                    pq.enqueue([nei, new_prob]);
                }
            }
        }

        return 0.0;
    }
}
