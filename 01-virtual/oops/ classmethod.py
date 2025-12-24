class ChaiOrder:

    def __init__(self,tea_type,sweetness,size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size


    @classmethod

    def from_dict(cls,order_data):
        return cls(
        order_data['tea_type'],
        order_data['sweetness'],
        order_data['size'])
        

    @classmethod   

    def from_str (cls, order_str):
        tea_type, sweetness , size = order_str.split('-')
        return cls(
            tea_type, sweetness ,size
        )


class ChaiUtils:
    @staticmethod

    def is_valid(size):
        return size in ["large", 'small', 'medium']

print(ChaiUtils.is_valid('medium'))        

order1 = ChaiOrder.from_dict({'tea_type': 'Lemon', 'sweetness': 'mild' ,'size': 'large'}) 

order2 = ChaiOrder.from_str('Ginger - Strong - small')

order3 = ChaiOrder('Honey', 'low' , 'medium')

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)



