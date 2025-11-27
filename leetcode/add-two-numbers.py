# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # collect digits from l1
        list_1 = []
        p1 = l1                      # changed: self.l1 -> l1
        while p1 is not None:
            list_1.append(p1.val)    # changed: list1.appendp -> list_1.append
            p1 = p1.next

        # collect digits from l2
        list_2 = []
        p2 = l2                      # changed: self.l2 -> l2
        while p2 is not None:
            list_2.append(p2.val)    # changed: list2.append -> list_2.append
            p2 = p2.next

        # build ints from reversed digits (because lists are in reverse order)
        n1 = int(''.join(str(d) for d in reversed(list_1))) if list_1 else 0
        n2 = int(''.join(str(d) for d in reversed(list_2))) if list_2 else 0
        total = n1 + n2

        # build result linked list from total (also reversed digits)
        dummy = ListNode(0)
        curr = dummy
        for ch in reversed(str(total)):
            curr.next = ListNode(int(ch))
            curr = curr.next

        return dummy.next