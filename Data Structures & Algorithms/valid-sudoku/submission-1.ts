class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board: string[][]): boolean {
        for (const row of board) {
            const set = new Set();
            for (const char of row) {
                if (char != '.' && set.has(char)) {
                    return false;
                }
                set.add(char);
            }
        }

        for (let i = 0; i < board.length; ++i) {
            const set = new Set();
            for (let j = 0; j < board[i].length; ++j) {
                if (board[j][i] != '.' && set.has(board[j][i])) {
                    return false;
                }
                set.add(board[j][i]);
            }
        }
        console.log("here");

        for (let quad_row = 0; quad_row < 2; quad_row += 3) {
            for (let quad_col = 0; quad_col < 2; quad_col += 3) {
                const set = new Set();
                console.log("new quad");
                for (let i = quad_row * 3; i < quad_row * 3 + 3; ++i) {
                    console.log("new row");
                    for (let j = quad_col * 3; j < quad_col * 3 + 3; ++j) {
                        console.log("quad_col * 3 + 2", quad_col * 3 + 2);
                        console.log("i: ", i);
                        console.log("j: ", i);
                        if (board[i][j] != '.' && set.has(board[i][j])) {
                            return false;
                        }

                        set.add(board[i][j]);
                    }
                }
            }
        }
        
        return true;
    }
}
