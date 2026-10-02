# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        stack=[]
        slow=head
        fast=head

        while fast and fast.next:
            stack.append(slow.val)
            slow=slow.next
            fast=fast.next.next
            
        if fast:
            slow=slow.next

        while stack:
            if stack[-1]!=slow.val:
                return False
            else:
                stack.pop()
                slow=slow.next
        return True
        