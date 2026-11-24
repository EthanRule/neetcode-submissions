class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    swimInWater(grid: number[][]): number {
        // Input size is small, can brute force:
        let t: number = 0;

        while (true) {
            const visited: boolean[][] = Array.from({ length: grid.length }, () => Array(grid.length).fill(false));
            if (this.pathExists(grid, t, 0, 0, visited)) return t;
            t++;
        }

        return t;
    }

    pathExists(grid: number[][], t: number, i: number, j: number, visited: boolean[][]): boolean {
        const n = grid.length;
        // Explore each index from current where
        if (i < 0 || i == grid.length || j < 0 || j == grid.length) return false;
        if (visited[i][j] || grid[i][j] > t) return false;
        if (i === n - 1 && j === n - 1) return true;

        visited[i][j] = true;

        return (
            this.pathExists(grid, t, i, j+1, visited) ||
            this.pathExists(grid, t, i, j-1, visited) ||
            this.pathExists(grid, t, i+1, j, visited) ||
            this.pathExists(grid, t, i-1, j, visited)
        )
    }
}
