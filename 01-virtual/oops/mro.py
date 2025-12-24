class A:
    label =  'A: Base Class'


class B(A):
    label = 'B: Lemon flavour'


class C (A):
    label = 'C: Honey flavour'  


class D (B,C):
    pass



flavour = D()
print(flavour.label)
print(D.__mro__)


# it calls very first class which is inhereting
