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
    public boolean isPalindrome(ListNode head) {
        // 1. Initialize currentNode to head
        ListNode currentNode = head;

        // 2. ArrayList because size of the array is unknown
        List<Integer> arrayList = new ArrayList<>();

        // 3. Start converting LinkedList to ArrayList
        // 3.1 Iterate over all the nodes repeatedly until last node
        while(currentNode != null) {
            // 3.2 `val` gets the currentNode's value
            int nodeValue = currentNode.val;
            // 3.3 Collect in the arrayList
            arrayList.add(nodeValue);
            // 3.4 Traverse to the next node
            currentNode = currentNode.next;
        }

        // 4. Prepare to check if the arrayList is palindrome or not
        // 4.1 Determine size of the list
        int arrayLength = arrayList.size();

        // 4.2 Iterate over the list from 0 through halfway
        // and compare elements from front and back
        for(int i = 0; i < arrayLength/2; i++) {
            // 4.2.1 `.equals` ensures negative numbers are compared
            if(!arrayList.get(i).equals(arrayList.get(arrayLength - i - 1))) {
                return false;
            }
        }

        return true;
    }
}
