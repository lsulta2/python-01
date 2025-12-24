class BaseChai:
    def __init__(self,type_):
        self.type = type_

    def prepare(self) :
        print(f'Preparing {self.type} chai...')  


# child class

class MasalaChai(BaseChai):
    def add_spices(self):
        print( 'Adding cardamom, ginger, lemom')



# composition

class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls('Regular')

    def serve(self):
        print(f'Serving {self.chai.type} in the shop.') 
        self.chai.prepare()   



class FancyShop(ChaiShop) :
    chai_cls = MasalaChai 


shop = ChaiShop()
fancy = FancyShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()

