import java.util.Random;

class Solution {
    ListNode head;
    Random rand;

    public Solution(ListNode head) {
        this.head = head;
        this.rand = new Random();
    }

    public int getRandom() {
        int result = head.val;
        ListNode curr = head.next;
        int i = 2;

        while (curr != null) {
            // pick current node with probability 1/i
            if (rand.nextInt(i) == 0) {
                result = curr.val;
            }
            curr = curr.next;
            i++;
        }

        return result;
    }
}