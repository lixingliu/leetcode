# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        temp = ListNode()
        tempHead = temp
        temp.val = head.val
        head = head.next
        while head:
            if temp.val == head.val:
                head = head.next
            else:
                temp.next = ListNode()
                temp = temp.next
                temp.val = head.val
                head = head.next



        return tempHead