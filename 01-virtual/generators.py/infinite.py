def infinite_chai():
    count = 1
    while True:
        yield f'Refil num: {count}'
        count+=1

refill = infinite_chai()  

for _ in range(5):
    print (next(refill))

orginal = infinite_chai()

for _ in range(6):
    print (next(orginal))