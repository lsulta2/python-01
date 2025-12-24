class Chai:
    def __init__(self,type_,strength):
        self.type = type_
        self.strength = strength


# code duplication
class GingerChai(Chai):
    def __init__(self,type_,strength, spice_level):
        self.type = type_
        self.strength = strength
        self.spice_level= spice_level


# explicit

class LemonChai(Chai):
    def __init__(self, type_, strength , flavour):
        Chai.__init__(self, type_, strength)
        self.flavour= flavour


#   super

class MasalaChai(Chai):
    def __init__(self,type_, strength, add_spices):
        super.__init__(type_,strength)
        self.add_spices = add_spices     