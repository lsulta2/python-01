def chai_type(): 
    type = 'Ginger tea'
    print(f'inside function {type}')
    # local scope

chai_type()
type = 'Lemon tea'
# global scope
print(f'outside function {type}')



# nested function

def order_type():
    order = 'Tea'  
    def tea_type():
        type = 'Lemon tea'
        print('Local Scope:', type) 

    tea_type()  
    print('Enclosing Scope:', order)

best_seller = 'Masala Tea'    
order_type()
print ('Global Scope:', best_seller)
