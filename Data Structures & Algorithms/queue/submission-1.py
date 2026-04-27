class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if self.head:
            return False
        return True

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def pop(self) -> int:
        val = 0

        #zero node
        if not self.head:
            return -1

        #single node
        if self.head == self.tail:
            val = self.head.val
            self.head = None
            self.tail = None
            return val
        
        #multi node
        cur = self.head
        while cur.next.next:
            cur = cur.next
        val = self.tail.val
        self.tail = cur
        self.tail.next = None
        return val
        

    def popleft(self) -> int:
        val = 0
        if not self.head:
            return -1
        val = self.head.val
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return val
            
