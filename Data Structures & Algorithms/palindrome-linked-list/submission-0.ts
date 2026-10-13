/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
class Solution {
    /**
     * @param {ListNode} head
     * @return {boolean}
     */
    isPalindrome(head: ListNode | null): boolean {
        const nodes = [];
        while (head) {
            nodes.push(head.val);
            head = head.next;
        }

        let i = 0;
        let j = nodes.length - 1;

        while (i < j) {
            if (nodes[i] != nodes[j]) {
                return false;
            }

            i++;
            j--;
        }

        return true;
    }
}
