from Pizzas import Pizza

class Decorator(Pizza):
    def __init__(self, component, name, cost):
        self.component = component
        super().__init__(name, cost)

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Olive(Decorator):
    def __init__(self,  component):
        super().__init__(component, "Olive", 10)


class Mushroom(Decorator):
    def __init__(self,  component):
        super().__init__(component, "Mushroom", 19)


class GoatCheese(Decorator):
    def __init__(self,  component):
        super().__init__(component, "GoatCheese", 7)


class Meat(Decorator):
    def __init__(self,  component):
        super().__init__(component, "Meat", 27)


class Onion(Decorator):
    def __init__(self,  component):
        super().__init__(component, "Onion", 3)


class Corn(Decorator):
    def __init__(self,  component):
        super().__init__(component, "Corn", 14)

