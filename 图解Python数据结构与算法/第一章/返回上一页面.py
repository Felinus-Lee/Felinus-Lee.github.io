class Browser:  
    def __init__(self):  
        self.history = []  
        self.current_page = None  
      
    def visit_page(self, page):  
        self.history.append(self.current_page)  
        self.current_page = page  
      
    def go_back(self):  
        if len(self.history) > 0:  
            self.current_page = self.history.pop()  
        else:  
            print("Can't go back anymore.")