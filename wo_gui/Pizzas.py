class Pizza:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.name


class Classic(Pizza):

    def __init__(self):
        super().__init__("Classical Pizza", 55)


class Margarita(Pizza):

    def __init__(self):
        super().__init__("Margarita Pizza", 85)


class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__("Turkish Pizza", 70)


class PlainPizza(Pizza):
    def __init__(self):
        super().__init__("Plain Pizza", 40)
