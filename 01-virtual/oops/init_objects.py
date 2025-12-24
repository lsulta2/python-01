class Chaiorder:
    def __init__(self, type_, size):
        self. type = type_
        self. size = size

    def summary(self):
        return f'{self.size} ml of {self.type} chai'


order_one = Chaiorder('Lemon', 109)
print(order_one.summary())

order_two = Chaiorder('Ginger', 200)
print(order_two.summary())

