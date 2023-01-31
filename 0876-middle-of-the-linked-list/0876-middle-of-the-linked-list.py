class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = [] 
        while head:
            nodes.append(head) 
            head = head.next
        middle = len(nodes)//2 
        return nodes[middle] 