def chai_status(cups_left):
    if cups_left == 0 :
        return 'Sorry, We do not have tea.'
    return 'Chai is ready'

print (chai_status(0))
print (chai_status(10))



def my_func():
    return 10, 25 , 35


num1, num2, num3 = my_func ()
print ('Num1:' , num1)
print ('Num2:' , num2)
print ('Num3:' , num3)