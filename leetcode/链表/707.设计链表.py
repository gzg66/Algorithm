#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class MyLinkedList:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def get(self, index: int) -> int:
        if index < 0 or self is None:
            return -1
        
        i, pre = 0, self
        while pre is not None:
            if i == index:
                return pre.val
            i += 1
            pre = pre.next
        
        return -1

    def addAtHead(self, val: int) -> None:
        n1 = MyLinkedList(val, self)
        self = n1

    def addAtTail(self, val: int) -> None:
        n1 = MyLinkedList(val)
        if head is None:
            head = n1
            return
        
        pre = head
        while pre.next is not None:
            pre = pre.next

        pre.next = n1

    # def addAtIndex(self, index: int, val: int) -> None:


    # def deleteAtIndex(self, index: int) -> None:



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

