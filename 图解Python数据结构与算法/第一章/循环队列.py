class CircularQueue:  
    def __init__(self, k: int):  
        self.k = k  # 循环队列的容量  
        self.queue = [None] * k  # 初始化循环队列  
        self.head = -1  # 队头指针，初始值为-1，表示队列为空  
        self.tail = -1  # 队尾指针，初始值为-1，表示队列为空  
  
    def enqueue(self, value: int) -> bool:  
        if self.is_full():  
            return False  # 队列已满，无法进队  
        if self.is_empty():  
            self.head = 0  # 如果队列为空，将队头指针指向第一个元素的位置  
        self.tail = (self.tail + 1) % self.k  # 计算新的队尾指针位置  
        self.queue[self.tail] = value  # 在队尾插入元素  
        return True  
  
    def dequeue(self) -> bool:  
        if self.is_empty():  
            return False  # 队列为空，无法出队  
        if self.head == self.tail:  # 如果队列中只有一个元素，出队后将队头和队尾指针都指向-1，表示队列为空  
            self.head = -1  
            self.tail = -1  
            return True  
        self.head = (self.head + 1) % self.k  # 计算新的队头指针位置  
        return True  
  
    def is_empty(self) -> bool:  
        return self.head == -1 and self.tail == -1  # 如果队头和队尾指针都指向-1，表示队列为空  
  
    def is_full(self) -> bool:  
        return (self.tail + 1) % self.k == self.head  # 如果队列中下一个元素的位置是队头指针的位置，表示队列已满

cq = CircularQueue(3)  # 创建一个容量为3的循环队列  
print(cq.enqueue("张三"))  # True  
print(cq.enqueue("李四"))  # True  
print(cq.enqueue("王五"))  # True
print(cq.enqueue("赵六"))  # False，队列已满，无法进队     
print(cq.dequeue())  # True，出队1  
print(cq.dequeue())  # True，出队2  
print(cq.dequeue())  # True，出队3
print(cq.dequeue())  # False，队列为空，无法出队