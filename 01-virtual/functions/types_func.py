def pour_chai(n):

    if n == 0 :
        return 'All cups poured'
    return pour_chai(n-1)

print (pour_chai(4))

# filter

chai_type = ['ginger' , 'lemon', 'karak' , 'Irani','karak']

strong_chai = list(filter(lambda chai: chai == 'karak' , chai_type))
print(strong_chai)

