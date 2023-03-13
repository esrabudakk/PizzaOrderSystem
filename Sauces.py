from Decorator import Decorator

class Olive(Decorator):
    def __init__(self,  component):
        super().__init__(component, "Olive",10,"")

class Mushroom(Decorator):
    def __init__(self,  component):
        super().__init__(component, "Mushroom",19,"")

class Cheese(Decorator):
    def __init__(self,  component):
        super().__init__(component, "Cheese",7,"")

class Sausage(Decorator):
    def __init__(self,  component):
        super().__init__(component, "Sausage",27,"")

class Onion(Decorator):
    def __init__(self,  component):
        super().__init__(component, "Onion", 3,"")

class Corn(Decorator):
    def __init__(self,  component):
        super().__init__(component, "Corn",14,"")

class Pepper(Decorator):
    def __init__(self,  component):
        super().__init__(component, "Pepper",11,"")