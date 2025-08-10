# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
      d=ListNode(0)
      d.next=head
      curr=d
      while curr.next!=None:
        if curr.next.val==val:
            curr.next=curr.next.next
        else:
            curr=curr.next
      return d.next