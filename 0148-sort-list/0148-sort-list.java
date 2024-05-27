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
    public ListNode sortList(ListNode head) {
        if(head == null || head.next == null){
            return head;
        }

        List<Integer> list = new ArrayList<>();
        while (head != null){
            list.add(head.val);
            head = head.next;
        }

        Collections.sort(list, Collections.reverseOrder());

        ListNode answer = new ListNode(list.get(0));
        for (int i=1 ; i < list.size() ; i++){
            answer = new ListNode(list.get(i), answer);
        }
        return answer;
    }
}