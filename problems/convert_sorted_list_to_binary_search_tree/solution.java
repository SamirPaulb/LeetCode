class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        if(head == null)
            return null;
        
        ListNode mid = mid(head);
        TreeNode root = new TreeNode(mid.val);
        
        if(head == mid)
            return root;
        
        root.left = sortedListToBST(head);
        root.right = sortedListToBST(mid.next);
        return root;
    }
    
    public ListNode mid(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        ListNode prev=head;
        while(fast!=null && fast.next!=null){
            prev=slow;
            slow = slow.next;
            fast = fast.next.next;
        }
        
        if(prev != null)
            prev.next = null;
        
        return slow;
    }
}