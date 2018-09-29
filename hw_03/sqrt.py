def mysqrt(number):
    guess = number
    for i in range (10):
    #while guess != number**(1/2):
        guess = (guess + number/guess)/2
    #print (guess)
    return "The square root of  " + str(number) + " is " + str (guess)

for i in range (1,101):
    print (mysqrt(i))
    
    
    
    
    
    
    
    
    
    
    
    
'''guess = 1
    while guess != number**(1/2):
        guess = (guess + number/guess)/2
        print (guess)
    return "the square root of " + str(number)+ " is " +str(guess)

for i in range(20):
    print (myrqrt(i))'''
         
