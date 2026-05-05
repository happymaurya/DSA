/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        // Handle edge cases: empty list or single node
        if (head == null || head.next == null) {
            return head;
        }
      
        // Calculate the length of the linked list
        ListNode current = head;
        int length = 0;
        while (current != null) {
            length++;
            current = current.next;
        }
      
        k = k % length;
      
        if (k == 0) {
            return head;
        }
      
        ListNode fastPointer = head;
        ListNode slowPointer = head;
      
        for (int i = 0; i < k; i++) {
            fastPointer = fastPointer.next;
        }
      
    
        while (fastPointer.next != null) {
            fastPointer = fastPointer.next;
            slowPointer = slowPointer.next;
        }
      
        ListNode newHead = slowPointer.next;
      
        slowPointer.next = null;
      
        fastPointer.next = head;
      
        return newHead;
    }
}
