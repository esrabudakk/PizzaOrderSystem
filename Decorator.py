from Pizzas import Pizza


class Decorator(Pizza):
    def __init__(self, component, name, cost, description):
        self.component = component
        super().__init__(name, cost,description)

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_name(self):
        return Pizza.get_name(self)

