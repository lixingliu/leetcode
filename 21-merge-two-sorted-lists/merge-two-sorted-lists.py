# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #edge cases if list1 or list2 is Empty
        if list1 == None and list2 == None:
            return list1
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        #logic to merge two lists
        list3 = ListNode()  #initialize linkedlist to return
        list3Head = list3   #store the head to return
        #helper function to recursely search through linked list
        def helper(list1, list2, list3):
            if list1 == None and list2 == None:
                return
            if list1 == None and list2 != None:                
                list3.val = list2.val
                list2 = list2.next
            if list1 != None and list2 == None:
                list3.val = list1.val
                list1 = list1.next
            if list1 != None and list2 != None:
                if list1.val <= list2.val:
                    list3.val = list1.val
                    list1 = list1.next
                else:
                    list3.val = list2.val
                    list2 = list2.next
            if list1 != None or list2 != None:
                list3.next = ListNode()
                list3 = list3.next
            helper(list1, list2, list3)
        helper(list1, list2, list3)
        return list3Head