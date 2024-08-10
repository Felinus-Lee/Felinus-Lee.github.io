class Student:  
    def __init__(self, name, age, gender, student_id):  
        self.name = name  
        self.age = age  
        self.gender = gender  
        self.student_id = student_id
        self.next = None  
  
    def __str__(self):  
        return f'{self.name} ({self.gender}), {self.age}岁, 学号: {self.student_id}'