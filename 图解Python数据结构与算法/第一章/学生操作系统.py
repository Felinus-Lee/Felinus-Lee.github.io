class LinkedList:  
    def __init__(self):  
        self.head = None  
  
    def add_student(self, student):  
        if not self.head:  
            self.head = student  
        else:  
            current = self.head  
            while current.next:  
                current = current.next  
            current.next = student  
  
    def remove_student(self, name):  
        current = self.head  
        if current and current.name == name:  
            self.head = current.next  
            current = None  
            return True  
        prev = None  
        while current and current.name != name:  
            prev = current  
            current = current.next  
        if current:  
            prev.next = current.next  
            current = None  
            return True  
        return False  
  
    def update_student(self, name, age, gender):  
        current = self.head  
        while current and current.name != name:  
            current = current.next  
        if current:  
            current.age = age  
            current.gender = gender  
            return True  
        return False  
  
    def find_student(self, name):  
        current = self.head  
        while current and current.name != name:  
            current = current.next  
        if current:  
            return current  
        return None
    
    def print_student_list(student_list):  
        current = student_list.head  
        while current:  
            print(current)  
            current = current.next