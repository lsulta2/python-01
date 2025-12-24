def main_menu():
    yield 'Biriyani'
    yield 'Kacchi'
    yield 'Borhani'


def snacks():
    yield 'Singara'  
    yield 'Fuchka'
    yield 'Puri'



def full_menu() :  

    yield from main_menu()
    yield from snacks()  


for menu in full_menu():
    print (menu)   


def message():

    try: 
        while True:
            order = yield 'Waiting for food'


    except:
        print ('Now Close')


shop = message()
print(next(shop))
shop.close()
# close for cleanup memory
