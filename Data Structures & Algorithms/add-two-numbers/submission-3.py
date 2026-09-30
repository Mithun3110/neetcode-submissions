# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        car = 0
        while l2 or l1:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            op = val1 + val2 + car

            car = op//10
            tail.next = ListNode(op%10)

            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if car:
                tail.next = ListNode(car)

        return dummy.next