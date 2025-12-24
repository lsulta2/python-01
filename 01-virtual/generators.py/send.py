def chai_customer():
    print('Welcome! What chai do you like?')
    order = yield

    while True:
        print(f'Preparing: {order}')
        order = yield


shop = chai_customer()
next(shop)

shop.send("Masala Chai")
shop.send ('Lemon Chai')