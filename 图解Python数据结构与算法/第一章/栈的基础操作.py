class Stack:  
    def __init__(self):  
        self.stack = []  
    
    #入栈操作
    def push(self, item):  
        self.stack.append(item)  
    
    #出栈操作
    def pop(self):  
        if not self.is_empty():  
            return self.stack.pop()  
        else:  
            return None  
  
    #判断栈是否为空
    def is_empty(self):  
        return len(self.stack) == 0  

    #查看栈的尺寸
    def size(self):  
        return len(self.stack)