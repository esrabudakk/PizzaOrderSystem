class Pizza:

    def __init__(self, name, cost, description):
        self.name = name
        self.cost = cost
        self.description = description
    
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return self.cost

    def get_name(self):
        return self.name


class Margarita(Pizza):
    def __init__(self):
        super().__init__("Margarita Pizza", 55, "Delicious pizza sauce on delicious pizza dough, mozzarella cheese, oregano!")


class White(Pizza):
    def __init__(self):
        super().__init__("White Pizza", 85, "Delicious ricotta sauce, mozzarella cheese, romano cheese and parsley on delicious pizza dough!")


class Gamer(Pizza):
    def __init__(self):
        super().__init__("Gamer Pizza", 70, "Delicious pizza sauce on delicious pizza dough, mozzarella cheese, sausage, black olives, fresh mushrooms!")


class MixedSausage(Pizza):
    def __init__(self):
        super().__init__("Mixed Sausage Pizza", 40, "Delicious pizza sauce on delicious pizza dough, mozzarella cheese, sliced sausage, fresh mushrooms, black olives, freshly sliced green and red peppers!")

class FourCheese(Pizza):
    def __init__(self):
        super().__init__("4 Cheese Pizza", 40, "Delicious pizza sauce, cream, mozzarella cheese, feta cheese, parmesan cheese, sesame, mayonnaise on delicious pizza dough!")
