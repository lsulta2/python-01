class Fruits:
    color = 'red'
    taste = 'sweet'
    orgin = 'USA'

apple = Fruits()
apple.color = 'green'
apple.market = 'super shop'
print (f'Apple is {apple.color}') 
print(f'We find in apple at {apple.market}')

del apple.color
print(f'After del, Apple is {apple.color}')



