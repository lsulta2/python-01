from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(2)
    print(f"End of {name} chai brewing")

if __name__ == '__main__':
    # Create a list of processes inside the main guard
    chai_makers = [
        Process(target=brew_chai, args=(f'Chai makers {i+1}',))
        for i in range(3)
    ]

    # Start all processes
    for p in chai_makers:
        p.start()

    # Wait for all processes to complete
    for p in chai_makers:
        p.join()

    print('All processes are done')