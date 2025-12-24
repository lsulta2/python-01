class Friuts:
    color = 'green'

    def describe(self):
        return f'Apple is {self.color}'


apple = Friuts()
print(apple.describe())


red_apple = Friuts()
red_apple.color  = 'red'

print(Friuts.describe(red_apple))