import threading
import time


def take_orders():
    for i in range(1, 4):
        print(f'Taking orders for {i}')
        time.sleep(1)


def making_orders():
    for i in range(1, 4):
        print(f'making orders for {i}')
        time.sleep(2)


# creating thread

take_thread = threading.Thread(target=take_orders)
make_thread = threading.Thread(target = making_orders)


take_thread.start()
make_thread.start()

# wait for both untill finish
take_thread.join()
make_thread.join()

print(f'All orders taken and making order now')