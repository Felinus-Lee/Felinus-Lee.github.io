class LinkedList:
    def __init__(self):
        self.head = None

    #创建链表
    def createList(self, n):
        for i in range(n):
            node = Node(int(input(f"Enter data for node {i + 1}: ")))
            if self.head is None:
                self.head = node
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = node

    #输出链表
    def printList(self):
        current = self.head
        print("List: ", end="")
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()