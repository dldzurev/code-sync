# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list_a = set()
        while(headA != None):
            list_a.add(headA)
            headA = headA.next
     
        while(headB != None):
            if(headB in list_a):
                return headB
            headB = headB.next
        return None