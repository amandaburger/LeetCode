public class removeNthElementLL {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode returnList = new ListNode(0,head);
        ListNode temp = returnList;

        for(int i =0; i<n; i++){
            head = head.next;
        }
        //head= 3 temp = 0
        while(head!=null){
            head = head.next;
            temp = temp.next;
        }
      
        temp.next =temp.next.next;

        return returnList.next;
    }
}
