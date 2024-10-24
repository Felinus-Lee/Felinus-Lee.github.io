class Node:  
    def __init__(self, data=None):  
        self.data = data  
        self.next = None 
  
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

    #链表长度
    def length(self):
        position = self.head
        count = 0
        while position:
            count += 1
            position = position.next
        return count  
    
    #增加头部元素  
    def prepend(self, data):      
        new_node = Node(data)      
        new_node.next = self.head      
        self.head = new_node

    #增加尾部元素
    def append(self, data):  
        new_node = Node(data)  
        if self.head is None:  # 如果链表为空，则将新节点设置为头部节点  
            self.head = new_node  
        else:  
            current = self.head  
            while current.next is not None:  # 遍历链表找到最后一个节点  
                current = current.next  
            current.next = new_node  # 将最后一个节点的指针指向新节点
    
    #增加中间元素
    def insert(self, data, position):  
        if position <= 0:
            self.prepend(data)
        elif position >=self.length():
            self.append(position)
        else:
            pre = self.head
            count = 0
            while count < position - 1:
                count += 1
                pre = pre.next
            node = Node(data)
            node.next = pre.next
            pre.next = node

    #删除头部节点
    def delete_head(self):  
        if self.head is not None:  
            self.head = self.head.next  
        else:  
            print("链表为空，无法删除头部节点")  
    
    #删除中间节点
    def delete_middle(self, key):  
        if self.head is None:  
            print("链表为空，无法删除中间节点")  
            return  
        temp = self.head  
        count = 0  
        while temp is not None and count < key:  
            temp = temp.next  
            count += 1  
        if temp is None:  
            print("链表长度小于给定的中间节点位置")  
        elif temp.next is None:  
            print("给定的位置是最后一个节点，无法删除")  
        else:  
            temp.next = temp.next.next  
            return  
    
    #删除尾部节点
    def delete_end(self):  
        if self.head is None:  
            print("链表为空，无法删除尾部节点")  
            return  
        temp = self.head  
        while temp.next is not None:  
            temp = temp.next  
        temp.next = None  
        return
    
    #查找元素位置
    def find_position(self, data):  
        current = self.head  
        position = 0  
        while current is not None:  
            if current.data == data:  
                return position  
            current = current.next  
            position += 1  
        return -1  # 如果未找到，则返回-1

if __name__ == "__main__":  
    n = int(input("Enter the number of nodes: ")) #输入节点个数  
    linked_list = LinkedList()  
    linked_list.createList(n)  
    linked_list.printList()  
