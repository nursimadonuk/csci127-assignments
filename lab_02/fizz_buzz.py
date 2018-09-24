"""numbers from 1 to 100, write fizz instead of all numbers divisible by 3 and buzz instead
all numbers divisible by 5, so if its divisible by both we print fizzbuzz"""
#Nursima Donuk and Madison Chen

def fizzbuzz(max_value):
    count = 0
    while count <= max_value:
        if count % 15 == 0 :
            print ('FizzBuzz')
        elif count % 5 == 0 :
            print ('Buzz')
        elif count % 3 == 0 :
            print ('Fizz')
        else:
            print (max_value)
        count += 1
    return 'there are ' + str (max_value // 15) + ' FizzBuzzes printed'


print (fizzbuzz(100))
         