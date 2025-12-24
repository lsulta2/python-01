# save mamory
# don't want result immediately, lazy evulation
#do not use return, using yield

def get_chai():
    yield 'cup1' 
    yield 'cup2'
    yield 'cup3'


chai = get_chai()
# holding the referance
# using next to print it,

print(next(chai))
print(next(chai))
print(next(chai))

