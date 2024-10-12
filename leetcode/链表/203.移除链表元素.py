#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 头节点为空
        if head is None:
            return None
        
        # 是否删除若干个头节点
        # 头节点不为空且相等
        while head is not None and head.val == val:
            head = head.next

        # 判断是否全部删除
        if head is None:
            return head

        pre, next = head, head.next
        while next is not None:
            if next.val == val:
                pre.next = next.next
            else:
                pre = pre.next
            next = next.next
        
        return head
# @lc code=end

