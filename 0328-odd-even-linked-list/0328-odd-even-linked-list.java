class Solution {
    public ListNode oddEvenList(ListNode head) {
        // Edge cases
        if (head == null || head.next == null) {
            return head;
        }

        ListNode odd = head;           // odd index nodes
        ListNode even = head.next;     // even index nodes
        ListNode evenHead = even;      // save even list start

        // Rearranging nodes
        while (even != null && even.next != null) {
            odd.next = even.next;      // connect odd to next odd
            odd = odd.next;

            even.next = odd.next;      // connect even to next even
            even = even.next;
        }

        // Attach even list after odd list
        odd.next = evenHead;

        return head;
    }
}